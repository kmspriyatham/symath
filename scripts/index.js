$( document ).ready( function() {
    var results = document.getElementById("results");
    $(results).contents().find('body').html("<html><head><style>*{font-family:Arial,Helvetica;color:chocolate;}</style></head><body>>>&nbsp</body><html>");
    $("#link-home").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#home").offset().top
        }, 500);
    });
    $("#link-home2").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#home").offset().top
        }, 500);
    });
    $("#link-results2").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#results2").offset().top
        }, 500);
    });
    $("input.expression").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#results2").offset().top
        }, 500);
    });
    $("#link-slates").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#slates").offset().top
        }, 500);
    });
    $("#link-help").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#help").offset().top
        }, 500);
    });
    $("#link-credits").click(function() {
        event.preventDefault();
        $('html, body').animate({
            scrollTop: $("#credits").offset().top
        }, 500);
    });
        $( "input.expression" ).keypress(function( event ) {
            var exp = document.getElementById("expression")
        	if (event.keyCode == 13) {
                if (exp.value == "") {
                    event.preventDefault();
                } else if (exp.value == "clear") {
                    $(results).contents().find('body').html("<html><head><style>*{font-family:sans-serif;}</style></head><body>>>&nbsp</body><html>");
                    exp.value = "";
                    event.preventDefault();
                }
                else {
                    request = new XMLHttpRequest();
                    request.open("post", "/", false);
                    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
                    var expression = "expression=" + encodeURIComponent(escape(exp.value));
                    request.send(expression);
                    if (request.status == 200) {
                        if (request.responseText != "") {
                            $(results).contents().find('body').html($(results).contents().find('body').html() + exp.value + "<br>" + "&nbsp" + request.responseText + "<br>" + ">>" + "&nbsp");
                        } else {
                            $(results).contents().find('body').html($(results).contents().find('body').html() + exp.value + "<br>" + ">>" + "&nbsp");
                        }
                    }
                    exp.value = "";
                    event.preventDefault();
                }
                results.scrollTop = results.scrollHeight;
        	}
        });
    });