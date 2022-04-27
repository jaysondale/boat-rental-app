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

var dateClass = '.datechk'
$(document).ready(function() {
    $(window).scroll(function() {
    	checkFade();
    	checkNavScrolled();
    	checkNavHidden();
    });
	if (document.querySelector(dateClass).type !== 'date') {
		var oCSS = document.createElement('link');
		oCSS.type='text/css'; oCSS.rel='stylesheet';
		oCSS.href='//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/base/jquery-ui.css';
		oCSS.onload=function() {
			var oJS = document.createElement('script');
			oJS.type='text/javascript';
			oJS.src='//ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js';
			oJS.onload=function() {
				$(dateClass).datepicker();
			}
			document.body.appendChild(oJS);
		}
		document.body.appendChild(oCSS);
	}
});