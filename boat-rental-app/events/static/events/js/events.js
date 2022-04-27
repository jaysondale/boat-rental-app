$('.interested-button').submit(function(event){
    event.preventDefault();
    // Get the form element using jQuery selector
    var form = $(this);
    // Get the CSRF token value (needs to be passed into the post request)
    var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
    // Turn the form into a json format
    data = form.serialize();
    // Add the CSRF token
    data['csrfmiddlewaretoken'] = CSRFtoken;
    // Create post request
    var posting = $.post(form.attr('action'), data);
    // Callback function run when a response is recieved
    posting.done(function(data){
    	// Success code = 200 (defined in the view function)
        if (data === '200') {
        	// Manually increment the interested count by 1
        	let span = form.find('button').find('span'); // <-- Research jQuery selectors to understand the .find() function better
        	// Increment count by 1
        	span.text(parseInt(span.text()) + 1);
        }
        // If a failure code is returned, the number won't update
    });
}) 