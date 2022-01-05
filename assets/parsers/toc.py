from bs4 import BeautifulSoup

def create_toc(link_path):
    with open(link_path) as doc_html:
        doc = BeautifulSoup(doc_html, "html.parser")
    ## Getting an array of all the tags h1, h2, h3 in the program
    array_h = doc.find_all(['h1', 'h2', 'h3'])
    ## Create a new string that would be the resulting table of content html code
    toc_html = "<div>"
    ## Looping through the array of h1, h2, h3 tags to manipulate it
    for tag in array_h:
        linkid = "<a href=" + "\"#" + str(tag['id']) + "\""
        toc_html +=  linkid
        if str(tag.name) == "h1":
            p_id = "class=\"toc_lvl1\">" + str(tag.string)
            #print "hi"
        elif str(tag.name) == "h2":
            p_id = "class=\"toc_lvl2\">" + str(tag.string)
            #print "hii"
        elif str(tag.name) == "h3":
            p_id = "class=\"toc_lvl3\">" + str(tag.string)
            #print "hiii"
        toc_html += p_id
        toc_html += "</a>"
    toc_html += "</div>"
    edited = BeautifulSoup(toc_html, "html.parser")
    return edited.prettify()

print(create_toc("../docs/welcomefile.html"))
