$(window).on('load', function() {
	$('.toggle-button').click(function() {
		var $selected = $(this).parent().parent().find('.selected')
		// Disable active pane
		var $div = $('div[name=\'' + $selected.html() + '\']');
		$div.addClass('d-none');
		$div.removeClass('d-flex');
		$selected.removeClass('selected');
		$(this).addClass('selected');
		$div = $('div[name=\'' + $(this).html() + '\']');
		$div.addClass('d-flex');
		$div.removeClass('d-none');
	});
});