import webbrowser
import os

def generate_staff(name, login, birthday, bio):
    """
    This method is to generate a div for staff's bio on the website.
    Input: String - name, login, birthday, bio
    Output: HTML string that will be the div of each staff's bio
    """
    the_html = "<div class=\"person-container\">"
    if login == 'eberkowi':
        the_html += "<img id=\"" + str(login) + "\" src=\"assets/img/" + str(login) + "-char.png\" class=\"staff-pic\" />"
    else:
        the_html += "<img id=\"" + str(login) + "\" src=\"assets/img/" + str(login) + "-char.jpg\" class=\"staff-pic\" />"
    the_html += "<strong>" + str(name) + "</strong>"
    the_html += "<div class=\"cs-login\">" + "<a href=\"mailto:" + str(login) + "@cs.brown.edu\">" + str(login) + "</a>" + "</div>"
    the_html += "<div class=\"birthday\">" + str(birthday) + "</div>"
    the_html += "<p class=\"bio-text\">" + str(bio) + "</p>"
    the_html += "</div>"
    return the_html

def generate_list_of_staff_HTML():
    """
    This method is to create the list of staff on the website.
    Input: None
    Output: String, HTML string that will display everyone's information
    on the course website
    """
    list_of_staff = "<div class=\"staff-wrapper\">"
    list_of_staff += "<h2>Professor and HTAs</h2>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Professor Kathi Fisler", "kathi", "Comes every year", "I like teaching intro CS courses because I struggled a lot with CS when I first tried it in college. I'm glad I stuck with it.")
    list_of_staff += generate_staff("Elias Berkowitz", "eberkowi", "April 1", "Eli loves being outdoors, sleeping, and especially sleeping outdoors.")
    list_of_staff += "</div>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Heila Precel", "hprecel", "Oct 29", "Unlike Eli, Heila prefers to sleep indoors. She can often be found napping on couches in the CIT.")
    list_of_staff += generate_staff("Josh Pattiz", "jpattiz", "December 12", "I am a Junior interested in Systems design and mobile development. This is my third time TAing but my first time HTAing.")
    list_of_staff += "</div>"
    list_of_staff += "<h2>Undergraduate TAs</h2>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Amy Li", "ali62", "May 17", "Hi! My name is Amy, and I'm concentrating in CS-Econ. I'm from Rochester, NY, and I love playing piano, swimming, reading, and finding four leaf clovers.")
    list_of_staff += generate_staff("Julia Windham", "jwindha1", "January 26", "I'm a sophomore studying APMA-CS from the Bay Area and the DC Metro area. I like to bake bread and watch bad rom-coms.")
    list_of_staff += "</div>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Leo Ryu", "lryu", "January 31", "I grew up in San Diego, California and love spending time with family and friends, playing my guitar, and going to the beach as often as I can :)")
    list_of_staff += generate_staff("Nicole Cheng", "ncheng2", "September 23", "Nicole is a sophomore from New York City who loves coffee and jam sessions. Some of her favorite TV shows are \"How I Met Your Mother\", \"The Office\", and \"Psych\". Song of the semester: House of the Rising Sun - The Animals.")
    list_of_staff += "</div>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Nam Do", "ndo3", "Oct 14", "Nam from Vietnam is a sophomore who loves reading, going on hikes (especially the one to his fridge), and drinking coffee. He also loves Sufjan Stevens and public transportation.")
    list_of_staff += generate_staff("Rohan Jha", "rjha", "April 29", "I'm a junior from Seattle, WA, concentrating in Math-CS. Outside of class, I'm involved in Brown Space Engineering, and I also like to hike and see movies. I'm excited to meet everyone!")
    list_of_staff += "</div>"
    list_of_staff += "<div class=\"row-wrapper\">"
    list_of_staff += generate_staff("Valeria Tiourina", "vtiourin", "Feb 7", "I am a senior studying CS, and in my free time I like to dance ballroom, play tennis, and hang out with my friends :)")
    list_of_staff += "</div>"
    list_of_staff += "</div>"
    return list_of_staff

def change_staff_HTML(staff_html):
    """
    This method is to change the staff list HTML file with the
    staff HTML string generated earlier.
    Input: String, HTML file that contains all the bios of all the staff
    Output: The same HTML file
    """
    dirname = os.path.abspath(os.path.dirname(__file__))
    open_file_path = os.path.join(dirname, "../../partials/staff-list.html")
    with open(open_file_path, "w") as staff_list_file:
        #staff_list_file = open(open_file_path, "w")
        staff_list_file.write(staff_html)
        #staff_list_file.close()
    return staff_html

change_staff_HTML(generate_list_of_staff_HTML())
