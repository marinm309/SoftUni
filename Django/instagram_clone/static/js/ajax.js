$('.like').click(function(e){
    e.preventDefault()
    var this_ = $(this)
    var likeUrl = this_.attr('href')
    $.ajax({
        url: likeUrl,
        method: 'GET',
        data: {koza: likeUrl},
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
    $.ajax({
        url: commentUrl,
        method: 'POST',
        data: {csrfmiddlewaretoken: csrf, comment_text: $('.type-comments').val()},
        success: function(request){
            $(request.indf_comment).text(request.comments)
            $('.type-comments').val('')
        }
    });
});
