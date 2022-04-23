$('.like').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var likeUrl = this_.attr('href')
    $.ajax({
        url: likeUrl,
        method: 'GET',
        data: {},
        success: function(request){
            $(request.indf).text(request.likes)
        }
    });
});

$('.comment-btn').click(function(f){
    f.preventDefault()
    var comment = $(this)
    var commentUrl = comment.attr('data-href')
    var csrf = $('input[name=csrfmiddlewaretoken]').val()
    var elements = comment.attr('data-id');

    $.ajax({
        url: commentUrl,
        method: 'POST',
        data: {csrfmiddlewaretoken: csrf, comment_text: $('#' + elements).val()},
        success: function(request){
            $(request.indf_comment).text(request.comments)
            $('.type-comments').val('')
        }
    });
});

$('.single-comment-btn').click(function(z){
    z.preventDefault()
    var single_comment = $(this)
    var single_commentURL = single_comment.attr('data-href')
    var csrf = $('input[name=csrfmiddlewaretoken]').val()
    var single_elements = single_comment.attr('data-id');


    $.ajax({
        url: single_commentURL,
        method: 'POST',
        data: {csrfmiddlewaretoken: csrf, comment_text: $('#' + single_elements).val()},
        success: function(request){
            console.log(single_elements)
            location.reload();
            $('.type-comments').val('')
        }
    });
});
