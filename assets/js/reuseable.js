$(document).ready(function() {
    //$("#header-wrapper").on("load", "../pages/partials/header.html #header");
    loadReuseable();
    //chooseHeaderPic();
    $(document).ajaxStop(function() {

        $("#sidebar-open").click(function() {
            $("#sidebar").toggleClass('opened');
        });
    });


});

var chooseHeaderPic = function() {
    var header_pic_arr = ["(\'../img/header-pic.png\')", "(\'../img/header-pic1.gif\')", "(\'../img/header-pic2.jpg\')", "(\'../img/header-pic3.jpg\')"];
    var random_pic = header_pic_arr[Math.floor(Math.random() * header_pic_arr.length)];
    $(document).ajaxStop(function() {
        $("#header-pic").css("background-image", "url" + random_pic);
        //window.open($("#header-pic").css("background-image"));
        //alert($("#header-pic").css("background-image"));
    });

}

var loadReuseable = function() {
    //$("#header-wrapper").load("partials/header.html");
    //$("#footer-wrapper").load("partials/footer.html");
};

const sidebarSlide = () => {
    const menuButton = document.querySelector('.menu-button');
    const sidebar = document.querySelector('#sidebar');
    const navButtons = document.querySelectorAll("#sidebar div");

    // Open menu.
    menuButton.addEventListener('click', () => {
        sidebar.style.transform = (sidebar.style.transform == "none") ? "translateX(100%)" : "none";

        // Animate links.
        navButtons.forEach((link, index) => {
            console.log(index);
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navButtonFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
    });

    // Reset upon resize
    window.addEventListener("resize", function(){
        // console.log(window.innerWidth);
        if (window.innerWidth > 785) {
            // console.log("Resetting navbar...");
            sidebar.removeAttribute("style");
        }
    });
}

const moveFolderTab = () => {
    const tabHome = document.querySelector('#content-tab-bottom-home');
    const tab = document.querySelector('#content-tab-bottom');
    const contentWrapper = document.querySelector('#content-wrapper');

    if(tabHome) {
        tabHome.style.height = $('#content-wrapper').height();
    }
    if(tab) {
        tab.style.height = $('#content-wrapper').height();
    }

    window.addEventListener("resize", function(){
        if(tabHome) {
            tabHome.style.height = $('#content-wrapper').height();
        }
        if(tab) {
            tab.style.height = $('#content-wrapper').height();
        }
    });
}

sidebarSlide();
moveFolderTab();
