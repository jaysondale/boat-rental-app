$(".boat-image-wrapper").addClass('col-12');
$(".boat-detail-wrapper").hide();


$("#boat-button").click(() => {
	$(".boat-image-wrapper").removeClass('col-12');
	$(".boat-image-wrapper").addClass('col-6');
	$(".boat-detail-wrapper").show();
})