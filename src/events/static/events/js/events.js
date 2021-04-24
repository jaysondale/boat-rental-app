$('.interested-button').submit(function(event){
    event.preventDefault();
    let form = $(this);
    let posting = $.post(form.attr('action'), form.serialize);
    posting.done(function(data){
        
    });
}) 