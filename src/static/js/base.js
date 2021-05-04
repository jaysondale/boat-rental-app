function checkElementFade(el) {
	if (!$(el).hasClass('fadeInUp')) {
		$(el).addClass('fadeInUp');
	}
}

function checkFade() {
	$('.animatedFadeInUp').withinviewport().each(function(i) {
		setTimeout(() => {
			checkElementFade(this);
		}, i * 100);
	});
	$('.animatedEarly').withinviewport({bottom: -200}).each(function(i) {
		setTimeout(() => {
			checkElementFade(this);
		}, i * 100);
	});
}

var stickyNav = 0;
function checkNavScrolled(){
	if ($(window).scrollTop() > stickyNav) {
		$('header').addClass('scrolled');
	} else {
		$('header').removeClass('scrolled');
	}
}

// Store previous location
var LAST_POS = 0;
// Function will hide navbar if scroll direction = down
function checkNavHidden(){
	var curr_pos = $(window).scrollTop();
	if (curr_pos > LAST_POS && curr_pos > stickyNav) {
		$('header').addClass('hidden');
	} else {
		$('header').removeClass('hidden');
	}
	LAST_POS = curr_pos;
}
// Check fade, nav scrolled on load
$(window).on('load', () => {
	checkFade();
	checkNavScrolled();
});

$(document).ready(function() {
    $(window).scroll(function() {
    	checkFade();
    	checkNavScrolled();
    	checkNavHidden();
    });
});

$(document).addEventListener("scroll", () => {
	document.documentElement.dataset.scroll = window.scrollY;
});