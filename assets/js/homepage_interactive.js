/*
This is a JS script to add interactive elements to the homepage of the website.
*/

function addInteractive() {
    const allWindows = document.querySelectorAll('.window');
    allWindows.forEach((window) => {
        relatedX = window.querySelector('.window-x');
        relatedX.addEventListener('click', () => {
            console.log("Hiding window")
            window.classList.add('hidden')
        });
    });
}


addInteractive()