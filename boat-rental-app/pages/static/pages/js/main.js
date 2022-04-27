var BG_IMG_RATIO = 1.51185495; // <-- UPDATE THIS IF BACKGROUND IMAGE CHANGES!!!

function checkBackground() {
	let $bg = $('.home-bg');
	if ($bg.width() / $bg.height() > BG_IMG_RATIO) {
		$bg.addClass('home-bg-alt');
	} else {
		if ($bg.hasClass('home-bg-alt')) {
			$bg.removeClass('home-bg-alt');
		}
	}
}

$(document).ready(function() {
	// If viewport is wider than background image, change to width=100%
	checkBackground();
	$(window).resize(function() {
		checkBackground();
	});
});