import json
import os
from pyquery import PyQuery as PQ
import lxml

def dict_to_link(d):
    if ("name" not in d) or ("link" not in d):
        print(d)
        raise ValueError("All link dicts must have name and link")

    if d['link'] is None:
        link = PQ('<div>')
        link.text(d['name'])
    else:
        link = PQ('<a>')
        link.attr('href', d['link'])
        link.attr('target', '_blank')
        link.text(d['name'])

    return link


def item_to_row(item, columns):
    row = PQ('<tr>')
    for col in columns:
        td = PQ('<td>')
        cell = item[col]
        if not isinstance(cell, (str, list, dict)):
            raise ValueError('Parser can only handle strings, lists, and dictionaries')

        if isinstance(cell, dict):
            content = dict_to_link(cell)
        elif isinstance(cell, list):
            content = PQ('<ul>')
            for subcell in cell:
                li = PQ('<li>')
                li.html(dict_to_link(subcell))
                content.append(li)
        else: # must be a string
            content = PQ('<div>')
            content.text(cell)

        td.html(content)
        row.append(td)

    return row

def json_to_table(json_path, table_id, columns, descr):
    with open(json_path) as f:
        data = json.load(f)

    table = PQ('<table>')
    table.attr('id', table_id)

    # SET UP HEADER
    header = PQ('<tr>')
    for col in columns:
        th = PQ('<th>')
        th.text(col)
        header.append(th)

    table.append(header)

    # SET UP CONTENTS
    for item in data:
        if "Display" in item:
            if item["Display"]:
                table.append(item_to_row(item, columns))
    return table

def update_file(json_path, html_path, replace_id, content_id, columns, descr):
    new_table = json_to_table(json_path, content_id, columns, descr)
    with open(html_path) as f:
        try:
            full_html = PQ(f.read())
        except lxml.etree.ParserError:
            print('No HTML for %s, skipping' % descr)
            return
    # print(new_table)
    full_html.find('#%s' % replace_id).html(new_table)
    # print(new_table)
    txt = full_html.html(method='html')
    with open(html_path, 'w') as f:
        f.write(txt)

def set_headers_and_footers(base='/course/cs0111/www'):
    header_path = os.path.join(base, 'partials', 'header.html')
    footer_path = os.path.join(base, 'partials', 'footer.html')
    with open(header_path) as h, open(footer_path) as f:
        try:
            header_html = PQ(h.read())
            footer_html = PQ(f.read())
        except lxml.etree.ParserError:
            raise ValueError('Header/Footer files don\'t have valid HTML')

    with open('../json/course-pages.json') as f:
        d = json.load(f)

    for page in d:
        path = os.path.join(base, page)
        with open(path) as f:
            try:
                uhoh = f.read()
                full_html = PQ(uhoh)
                old_html = full_html.clone()
            except lxml.etree.ParserError:
                print('No HTML for %s, skipping' % page)
                return

        full_html.find('#header-wrapper').html(header_html)
        full_html.find('#footer-wrapper').html(footer_html)

        with open(path, 'w') as f:
            newc = full_html.html(method='html').encode('utf-8')
            try:
                f.write(newc)
            except:
                print('Error in parsing %s' % page)
                try:
                    f.write(old_html.html(method='html'))
                    raise
                except:
                    print('\tPyquery doesn\'t work on this page')
                    f.write(uhoh)
                    raise


update_file('../json/lectures.json',
            '../../lectures.html',
            'lectures-table-wrapper',
            'lectures-table',
            ['Date', 'Topic', 'Summary', 'Readings', 'Lecture Capture', 'Extras'],
            'Lectures')

update_file('../json/labs.json',
            '../../labs.html',
            'labs-table-wrapper',
            'labs-table',
            ['Lab', 'Additional Materials'],
            'Labs')

update_file('../json/assignments.json',
            '../../assignments.html',
             'assignments-table-wrapper',
             'homeworks-table',
             ['Assignment', 'Out', 'In', 'Support Docs'],
             'Homeworks')

update_file('../json/projects.json',
            '../../assignments.html',
             'projects-table-wrapper',
             'projects-table',
             ['Assignment', 'Out', 'In', 'Support Docs', 'Forms'],
             'Projects')

update_file('../json/drills.json',
            '../../assignments.html',
             'drills-table-wrapper',
             'drills-table',
             ['Assignment', 'Out', 'In', 'Solutions'],
             'Drills')

update_file('../json/workshops.json',
	    '../../lectures.html',
	    'workshops-table-wrapper',
	    'workshops-table',
	    ['Date', 'Topic', 'Presentation', 'Recording'],
	    'Workshops')


# set_headers_and_footers()
