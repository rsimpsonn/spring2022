/*
This is a JS script to add interactive elements to the window containers on pages
*/

function makeWindowsClosable() {
    const allWindows = document.querySelectorAll('.window');
    allWindows.forEach((aWindow) => {
        relatedX = aWindow.querySelector('.window-x');
        relatedX.addEventListener('click', () => {
            console.log("Hiding window")
            aWindow.classList.add('hidden')
        });
    });
}

class DraggableWindow {
    constructor(dragBar, elt) {
        this.dragBar = dragBar;
        this.elt = elt;
        this.initialX = 0;
        this.initialY = 0;
        this.currentX = 0;
        this.currentY = 0;
        this.xOffset = 0;
        this.yOffset = 0;
        this.active = false;
    }
}

function dragStartFunction(itemToDrag) {
    return (event) => {
        console.log("Drag start", event, itemToDrag)
        if (event.type == "touchstart") {
            itemToDrag.initialX = event.touches[0].clientX - itemToDrag.xOffset;
            itemToDrag.initialY = event.touches[0].clientY - itemToDrag.yOffset;
        } else {
            itemToDrag.initialX = event.clientX - itemToDrag.xOffset;
            itemToDrag.initialY = event.clientY - itemToDrag.yOffset;
        }
        if (itemToDrag.dragBar.contains(event.target)) {
            itemToDrag.active = true;
        }
    }
}

function deactivateDrag(allDraggableWindows) {
    return (event) => {
        console.log("deactivate", allDraggableWindows)
        allDraggableWindows.forEach((draggableWindow) => {
            draggableWindow.initialX = draggableWindow.currentX;
            draggableWindow.initialY = draggableWindow.currentY;
            draggableWindow.active = false;
        })
    }
}

function dragFunction(allDraggableWindows) {
    return (event) => {
        allDraggableWindows.forEach((aWindow) => {
            if (aWindow.active) {
                event.preventDefault();
                if (event.type === "touchmove") {
                    aWindow.currentX = event.touches[0].clientX - aWindow.initialX;
                    aWindow.currentY = event.touches[0].clientY - aWindow.initialY;
                } else {
                    aWindow.currentX = event.clientX - aWindow.initialX;
                    aWindow.currentY = event.clientY - aWindow.initialY;
                }
                aWindow.xOffset = aWindow.currentX;
                aWindow.yOffset = aWindow.currentY;
                setTranslate(aWindow.currentX, aWindow.currentY, aWindow.elt);
            }
        })
    }
}

function setTranslate(xPos, yPos, el) {
    console.log(el.style.transform)
    el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}

function makeWindowsDraggable() {
    const allWindows = document.querySelectorAll('.window');
    const allDraggableWindows = Array.from(allWindows).map((window) => {
        let dragBar = window.querySelector('.window-top-bar');
        return draggableWindow = new DraggableWindow(dragBar, window);
    })
    const mainArea = document.querySelector('main');
    mainArea.addEventListener('touchend', deactivateDrag(allDraggableWindows), false);
    mainArea.addEventListener('touchmove', dragFunction(allDraggableWindows), false);
    mainArea.addEventListener('mouseup', deactivateDrag(allDraggableWindows), false);
    mainArea.addEventListener('mousemove', dragFunction(allDraggableWindows), false);

    allDraggableWindows.forEach((draggableWindow) => {
        console.log(draggableWindow)
        draggableWindow.dragBar.addEventListener("touchstart", dragStartFunction(draggableWindow), false);
        draggableWindow.dragBar.addEventListener("mousedown", dragStartFunction(draggableWindow), false);
    });
}

makeWindowsClosable()
makeWindowsDraggable()