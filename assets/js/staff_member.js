$(document).ready(function() {
    $("#staff-mega-wrapper").load("partials/staff-list.html");
    staffPic();
});

var staffPic = function() {
    $(document).ajaxStop(function() {
        var cslogin_array = ["kathi", "eberkowi", "hprecel", "jpattiz", "ali62", "jwindha1", "lryu", "ncheng2", "ndo3", "rjha", "vtiourin"];
        $.each(cslogin_array, function(index, login) {
            var element = $("#" + login);
            var hover_source = "assets/img/" + login + "-pic.jpg";
            if (login == 'eberkowi') {
                var normal_source = 'assets/img/' + login + '-char.png';
            }
            else {
                var normal_source = "assets/img/" + login + "-char.jpg";
            }
            element.hover(function() {
                element.attr("src", hover_source);
            }, function() {
                element.attr("src", normal_source);
            });
        });
    });
}
