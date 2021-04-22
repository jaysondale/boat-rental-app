// Get radio buttons vals
let RADIO_OPTIONS = ["new_user", "existing_user"];

// Hide new user area
$('#new-user-area').hide()

$(window).on('load', () => {
	$('.default-btn').addClass('active');
	$("#radiobuttons input[name='options']").click(() => {
		let val = $("input:radio[name='options']:checked").val();
		
		let nya = $("#new-user-area");
		let eya = $("#existing-user-area");
		// If new user button selected
		if (val === RADIO_OPTIONS[0]) {
			nya.show();
			eya.hide()
		} else if (val === RADIO_OPTIONS[1]) {
			// If existing user button selected
			eya.show()
			nya.hide()
		}
	});
});