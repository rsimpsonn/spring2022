/*
This is a JS script to add interactive elements to the homepage of the website.
*/

function makeWindowsClosable() {
    const allWindows = document.querySelectorAll('.window');
    allWindows.forEach((window) => {
        relatedX = window.querySelector('.window-x');
        relatedX.addEventListener('click', () => {
            console.log("Hiding window")
            window.classList.add('hidden')
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

function dragEndFunction(itemToDrag) {
    return (event) => {
        console.log("Drag end", event, itemToDrag)
        itemToDrag.initialX = itemToDrag.currentX;
        itemToDrag.initialY = itemToDrag.currentY;
        itemToDrag.active = false;
    }
}

function dragFunction(itemToDrag) {
    return (event) => {
        console.log(itemToDrag.active)
        if (itemToDrag.active) {
            event.preventDefault();
            if (event.type === "touchmove") {
                itemToDrag.currentX = event.touches[0].clientX - itemToDrag.initialX;
                itemToDrag.currentY = event.touches[0].clientY - itemToDrag.initialY;
            } else {
                itemToDrag.currentX = event.clientX - itemToDrag.initialX;
                itemToDrag.currentY = event.clientY - itemToDrag.initialY;
            }
            itemToDrag.xOffset = itemToDrag.currentX;
            itemToDrag.yOffset = itemToDrag.currentY;
            setTranslate(itemToDrag.currentX, itemToDrag.currentY, itemToDrag.elt);
        }
    }
}

function setTranslate(xPos, yPos, el) {
    console.log(el.style.transform)
    el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}

function makeWindowsDraggable() {
    const allWindows = document.querySelectorAll('.window');
    const draggableWindows = Array.from(allWindows).map((window) => {
        let dragBar = window.querySelector('.window-top-bar');
        return draggableWindow = new DraggableWindow(dragBar, window);
    })
    const content = document.querySelector('#main')

    allWindows.forEach((window) => {
        let dragBar = window.querySelector('.window-top-bar')
        let draggableWindow = new DraggableWindow(dragBar, window);
        dragBar.addEventListener("touchstart", dragStartFunction(draggableWindow), false);
        dragBar.addEventListener("touchend", dragEndFunction(draggableWindow), false);
        dragBar.addEventListener("touchmove", dragFunction(draggableWindow), false);

        dragBar.addEventListener("mousedown", dragStartFunction(draggableWindow), false);
        dragBar.addEventListener("mouseup", dragEndFunction(draggableWindow), false);
        dragBar.addEventListener("mousemove", dragFunction(draggableWindow), false);
    });
}


makeWindowsClosable()
    // makeWindowsDraggable()