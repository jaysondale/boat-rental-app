function checkElementFade(el) {
	if (!$(el).hasClass('fadeInUp')) {
		$(el).addClass('fadeInUp');
	}
};


function checkFade() {
	els = $('.animatedFadeInUp').withinviewport().each(function(i) {
		setTimeout(() => {
			checkElementFade(this);
		}, i * 100);
	});
}

// Check fade on load
$(window).on('load', checkFade);

// Re-assess fade on page scroll
$(window).scroll(checkFade)