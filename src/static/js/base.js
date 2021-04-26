function checkElementFade(el) {
	if (!$(el).hasClass('fadeInUp')) {
		$(el).addClass('fadeInUp');
	}
}

function checkFade() {
	els = $('.animatedFadeInUp').withinviewport().each(function(i) {
		setTimeout(() => {
			checkElementFade(this);
		}, i * 100);
	});
}
// Check fade on load
$(window).on('load', checkFade);

$(document).ready(function() {
	var stickyNav = $('header').offset().top;
    $(window).scroll(function() {
    	checkFade();
        if ($(window).scrollTop() > stickyNav) {
            $('header').addClass('scrolled');
        } else {
            $('header').removeClass('scrolled');
        }
    });
});