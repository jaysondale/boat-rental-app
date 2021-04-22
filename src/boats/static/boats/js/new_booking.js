// Get radio buttons vals
let RADIO_OPTIONS = ["new_user", "existing_user"];

// Hide new user area
$('#new-user-area').hide();

$(window).on('load', () => {
	$('.default-btn').addClass('active');
	$("#radiobuttons input[name='options']").click(() => {
		let val = $("input:radio[name='options']:checked").val();
		
		let $nua = $("#new-user-area");
		let $eua = $("#existing-user-area");

		let $nuf = $('.new-user-field');
		let $euf = $('.existing-user-field');
		// If new user button selected
		if (val === RADIO_OPTIONS[0]) {
			$nua.show();
			$eua.hide();
			$nuf.attr('required')
			$euf.removeAttr('required');
		} else if (val === RADIO_OPTIONS[1]) {
			// If existing user button selected
			$eua.show();
			$nua.hide();
			$euf.attr('required');
			$nuf.removeAttr('required');
		}
	});
});