"""
This file is to convert json to html so that we can dynamically
create tables in assignments and lectures pages
"""

from json2html import *
import json
from collections import OrderedDict
import webbrowser
import os
import lxml
from bs4 import BeautifulSoup
from pyquery import PyQuery as PQ

def convert_json_to_html(link_path, attributes=""):
    """
    Purpose: Use json2html to convert a json file to a table
    Input: (1) String, path to the JSON file (2) String,
    attributes to the table that will be created
    Output: String, HTML file that is converted from the JSON file
    """
    # Open the json file
    with open(link_path) as json_file:
        table = json.load(json_file, object_pairs_hook=OrderedDict)
    # Convert the json file using the opened file and using input attributes
    try:
        table = list(filter(lambda item: item['Display'], table))
        for item in table:
            item.pop("Display")
    except KeyError:
        print 'Object does not have Display value (%s)' % link_path
        print 'Continuing.'
    result = json2html.convert(json = table, table_attributes=attributes)
    # Returning the string
    return result

def beautify_html(html_string):
    """
    Purpose: To take a HTML table with nested tables (of text and
    the link that comes with it) to make a new HTML without nested HTML
    tables
    Input: String, HTML table with nested tables
    Output: String, HTML table without nested tables
    """
    # To put the HTML string to BeautifulSoup type for work
    doc = BeautifulSoup(html_string, "html.parser")
    # Looking for tables in the file
    array_tables = doc.find_all("table")
    for table in array_tables:
        # If table is nested in a bigger table
        if table.parent.name == "td":
            new_script = ""
            tr_s = table.find_all("tr")
            ## Case when there is only one link and name
            if tr_s[0].find_all("td") != []:
                string = str(tr_s[0].find("td").string)
                if string != "---":
                    new_script += "<a target=\"_blank\">"
                    new_script += str(tr_s[0].find("td").string)
                    new_script += "</a>"
                    new_script = BeautifulSoup(new_script, "html.parser")
                    new_script.find("a")['href'] = str(tr_s[1].find("td").string)
                else:
                    new_script += "---"
                    new_script = BeautifulSoup(new_script, "html.parser")
            ## Case when there are multiple links and name
            else:
                # Make a list of the different links
                new_script = "<ul>"
                for tr in tr_s:
                    td_s = tr.find_all("td")
                    if td_s != []:
                        if str(td_s[0].string) != "---":
                            addition = "<li><a target=\"_blank\" href=\"" + str(td_s[1].string) + "\">" + str(td_s[0].string) + "</a></li>"
                        else:
                            addition = "---"
                        new_script += addition
                new_script += "</ul>"
                # Soupify the modified HTML code to replace with the soup table
                new_script = BeautifulSoup(new_script, "html.parser")
            # Replace the soup table with the new code (link or not link)
            table.replace_with(new_script)
    # Returning HTML string without nested tables
    return str(doc)

"""
The three methods below are for updating the html files
that are converted from the json files - called whenever
the file is run
"""

def update_file(html_path, json_path, html_id, generate_id, descr):
    attrs = "id=\"%s\" class=\"jsontable table\"" % generate_id
    html_table = convert_json_to_html(json_path, attrs)
                                    
    clean_table = beautify_html(html_table)
    try:
        new_html = PQ(clean_table)
    except lxml.etree.ParserError:
        print 'No %s JSON objects to display, skipping' % descr
        return

    with open(html_path) as f:
        try:
            old_html = PQ(f.read())
        except lxml.etree.ParserError:
            print 'No HTML for %s, skipping' % descr
            return

    old_html.find(html_id).html(new_html)
    with open(html_path, "w") as f:
        f.write(old_html.html(method='html'))

#update_file('/course/cs0111/www/pages/lectures.html',
#            '/course/cs0111/www/assets/json/lectures.json',
#            '#lectures-table-wrapper',
#            'asgnmnt-tble',
#            'homework')
#sys.exit(0)

def update_assignments():
    json_path = "../json/assignments.json"
    dirname = os.path.abspath(os.path.dirname(__file__))
    html_path = os.path.join(dirname, "../../pages/partials/asgnmnt-tble.html")
    assignments_html = beautify_html(convert_json_to_html(json_path, "id=\"asgnmnt-tble\" class=\"jsontable table\""))
    try:
        new_html = PQ(assignments_html)
    except lxml.etree.ParserError:
        print 'No homeworks to display, skipping'
        return
    with open(html_path) as f:
        try:
            old_html = PQ(f.read())
        except lxml.etree.ParserError:
            print 'No JSON for assignments, skipping'
            return

    old_html.find('#assignments-table-wrapper').html(new_html)
    with open(html_path, "w") as assignments_html_file:
        assignments_html_file.write(str(assignments_html))

    return assignments_html

def update_projects():
    json_path = "../json/projects.json"
    dirname = os.path.abspath(os.path.dirname(__file__))
    html_path = os.path.join(dirname, "../../pages/partials/project-tble.html")
    projects_html = beautify_html(convert_json_to_html(json_path, "id=\"project-tble\" class=\"jsontable table\""))
    try:
        new_html = PQ(projects_html)
    except lxml.etree.ParserError:
        print 'No JSON for projects, skipping'
        return

    with open(html_path) as f:
        try:
            old_html = PQ(f.read())
        except lxml.etree.ParserError:
            print 'No html for projects, skipping'
            return

    old_html.find('#projects-table-wrapper').html(new_html)
    with open(html_path, "w") as projects_html_file:
        projects_html_file.write(str(new_html))

    return projects_html

def update_lectures():
    json_path = "../json/lectures.json"
    dirname = os.path.abspath(os.path.dirname(__file__))
    html_path = os.path.join(dirname, "../../pages/partials/lec-tble.html")
    lectures_html = beautify_html(convert_json_to_html(json_path, "id=\"lec-tble\" class=\"jsontable table\""))
    try:
        new_html = PQ(lectures_html)
    except lxml.etree.ParserError:
        print 'No JSON for lectures, skipping'
        return

    with open(html_path) as f:
        try:
            old_html = PQ(f.read())
        except lxml.etree.ParserError:
            print 'No html for lectures, skipping'
            return

    old_html.find('#lectures-table-wrapper').html(new_html)
    with open(html_path, "w") as lectures_html_file:
        lectures_html_file.write(str(old_html))

    return lectures_html

def update_labs():
    json_path = "../json/labs.json"
    dirname = os.path.abspath(os.path.dirname(__file__))
    html_path = os.path.join(dirname, "../../pages/partials/lab-tble.html")
    labs_html = beautify_html(convert_json_to_html(json_path, "id=\"lab-tble\" class=\"jsontable table\""))
    new_html = PQ(labs_html)

    with open(html_path) as f:
        old_html = PQ(f.read())

    old_html.find('#labs-table-wrapper').html(new_html)
    with open(html_path, "w") as labs_html_file:
        labs_html_file.write(str(old_html))

    return labs_html

update_assignments()
update_projects()
update_lectures()
#update_labs()

#print beautify_html(convert_json_to_html("../json/assignments.json"))
