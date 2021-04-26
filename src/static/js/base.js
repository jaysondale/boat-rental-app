$(document).ready(function() {
	var stickyNav = $('header').offset().top;
    $(window).scroll(function() {
        if ($(window).scrollTop() > stickyNav) {
            $('header').addClass('scrolled');
        } else {
            $('header').removeClass('scrolled');
        }
    });
});