var DATA_TABLE = null;
var DELETE_URL = null;

$(window).on("load", function() {
	$('.booking-view-btn').click(function() {
		// Update modal content with selected booking
		let bid = $(this).parent().parent().attr('booking_id');
		let conf_url = $(this).attr('conf_url');
		let get_url = '/manage_rental_bookings/get_booking_data/' + bid;
		$.get(get_url, function(data) {
			$('#booking-user-name').html(data['name'])
			// Find rental item index
			let opt_ind = 0
			$("option").each(function(i) {
				if ($(this).text() === data['rentalItem']) {
					opt_ind = $(this).val()
				}
			});
			// Select defaults
			$('#booking-rental-item').selectpicker('val', opt_ind.toString());
			$('#booking-start-day').val(data['startDay']);
			$('#booking-end-day').val(data['endDay']);

			// Activate form
			$('#booking-confirm-form').attr('action', conf_url) ;
		}).then(_ => {
			$('#view-booking-modal').modal("show");
		})
	});

	$('.cancel-booking').click(function() {
		let bid = DATA_TABLE.cell(DATA_TABLE.row($(this).parent()).index(), 8).data();
		console.log('deleting booking');
		$.ajax({url: DELETE_URL,
			type: 'post',
			data: {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value, 'bid': bid},
			success: function(response) {
					if (response['code'] == 400){
						alert('Error: Bad Request');
					}
					window.location.reload(true);
				}
			})
	})

	$('.view-toggle').click(function(i) {
		let val = $(this).val();
		$calview = $('#calendar-view')
		$listview = $('#list-view')
		if (val === 'cal') {
			$calview.show();
			$listview.hide();
			$(this).addClass('selected');
			$('.view-toggle[value=list').removeClass('selected');
		} else if (val === 'list') {
			$('#calendar-view').hide();
			$('#list-view').show();
			$(this).addClass('selected');
			$('.view-toggle[value=cal').removeClass('selected');
		}
	});

	// Calendar view is default
	$('#calendar-view').show();
	$('.view-toggle[value=cal').addClass('selected');
	$('#list-view').hide();

	// Calendar event hover
	$('.calendar-list').hover(function() {
		console.log($(this).attr('booking-id'));
		$('.calendar-list[booking-id=' + $(this).attr('booking-id') + "]").addClass('hovering');
	}, function() {
		$('.calendar-list[booking-id=' + $(this).attr('booking-id') + "]").removeClass('hovering');		
	})
});

$(document).ready(function() {
	// DataTable initiatlization
	var $table = $('#confirmed-bookings-table');
	DELETE_URL = $table.attr('ajax-delete');
	DATA_TABLE = $table.DataTable({
		ajax: {url: $table.attr('data-source'),
			dataSrc: 'data'
		},
		columns: [{ data: 'name' },
        { data: 'email' },
        { data: 'phone' },
        { data: 'rentalItem' },
        { data: 'startDay' },
        { data: 'endDay' },
        { data: 'price'},
        { data: null, 'defaultContent': '<button class="btn btn-danger cancel-booking">Cancel</button>'},
        { data: 'pk', visible: false, searchable: false }]
	});
})