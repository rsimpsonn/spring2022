/*
This is a JS script to render the current projects, drills, homeworks, etc. on the front page of the site
(index.html at the top level of the project). It will go through the JSON files containing assignments
and due dates and choose the most relevant ones to display based on the current time.
*/

/* 
NOTE FOR RUNNING LOCALLY:
In order for this to display properly, you must run python -m http.server within the terminal
from the top of the project. Then, visit localhost:8000/index.html and view the site from there
*/

const CURR_DATE = new Date()
const CURR_TIME = new Date().getTime()
const MILISECONDS_IN_24_HOURS = 86400000
const TESTING_RETRIEVAL = false
const RENDER_CURR_LAB = true

async function retrieveJson(filepath) {
    const response = await fetch(filepath);
    const data = await response.json();
    return data;
}

/**
 * Take the date format "mm/dd/yyyy" and convert it to a Javascript date
 * @param {String} date 
 * @param {boolean} setToMaxTime true = set the time to 11:59PM
 * @returns {Date}
 */
function cleanDate(date, setToMaxTime) {
    const dateInMS = new Date(date.split(" ")[1]).getTime()
    if (setToMaxTime) {
        return new Date(dateInMS + MILISECONDS_IN_24_HOURS - 1)
    } else {
        return new Date(dateInMS)
    }
}

function findCurrAssignment(allAssignments) {
    // filter to find all assignments that are within the current date range and are on display
    const withinDateRangeAndDisplayed = allAssignments.filter((assignment) => {
        outTime = cleanDate(assignment["Out"], false).getTime()
        inTime = cleanDate(assignment["In"], true).getTime()
        return (outTime - CURR_TIME >= 0) && (inTime - CURR_TIME <= 0) && assignment["Display"]
    })
    if (withinDateRangeAndDisplayed.length == 0) {
        return null
    } else {
        // In the case of multiple assignments in the date range, the first one will be chosen
        return withinDateRangeAndDisplayed[0]
    }
}

function renderCurrAssignment(domElementId, filepath) {
    retrieveJson(filepath)
        .then(data => {
            currentAssignment = data[0]
            if (!TESTING_RETRIEVAL) {
                currentAssignment = findCurrAssignment(data)
            }
            console.log(currentAssignment)
            if (currentAssignment != null) {
                renderAssignmentHelper(domElementId, currentAssignment)
            } else {
                // Can do something here if there is no assignment in the date range
            }
        })
}

// This can be used for assignments, drills, projects; not for labs
function renderAssignmentHelper(domElementId, currentAssignment) {
    // This can be done much easier in JQuery. Unfortunately, I do not know JQuery
    assignmentDiv = document.getElementById(domElementId)
    assignmentDiv.innerHTML = ""
    assignmentLink = document.createElement('a')
    assignmentLink.href = currentAssignment['Assignment']['link']
    assignmentLink.target = "_blank"
    assignmentTitle = document.createElement('strong')
    assignmentTitle.innerHTML = currentAssignment['Assignment']['name']
    assignmentLink.appendChild(assignmentTitle)
    assignmentDue = document.createElement('p')
    assignmentDue.innerHTML = currentAssignment['In']
        // assignmentDue = document.createTextNode("Due " + currentAssignment['In'])
    assignmentDiv.appendChild(assignmentLink)
    assignmentDiv.appendChild(assignmentDue)
}

function renderMostRecentLab() {
    const labJsonUrl = '/assets/json/labs.json'
    retrieveJson(labJsonUrl)
        .then(labs => {
            displayedOnly = labs.filter((lab) => lab["Display"])
            lastDisplayed = displayedOnly[displayedOnly.length - 1]
            labDiv = document.getElementById('current-lab')
            labDiv.innerHTML = ''
            labLink = document.createElement('a')
            labLink.href = lastDisplayed["Lab"]["link"]
            labLink.target = "_blank"
            labTitle = document.createElement('strong')
            labTitle.innerHTML = lastDisplayed["Lab"]["name"]
            labLink.appendChild(labTitle)
            labDiv.appendChild(labLink)
        })
}

async function renderAssignments() {
    renderCurrAssignment('current-homework', '/assets/json/assignments.json')
    renderCurrAssignment('current-project', '/assets/json/projects.json')
    renderCurrAssignment('current-drill', '/assets/json/drills.json')
    if (RENDER_CURR_LAB) {
        renderMostRecentLab()
    }
}

renderAssignments()