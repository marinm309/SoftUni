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
            $("#" + request.basic_indf + '6969').load(location.href + ' ' + "#" + request.basic_indf + '6969');
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
            $('.type-comments').val('')
            location.reload()
        }
    });
});

$('.single-post-comment-like-btn').click(function(m){
    m.preventDefault()
    var single_like = $(this)
    var single_likeURL = single_like.attr('href')

    $.ajax({
        url: single_likeURL,
        method: '',
        data: {},
        success: function(request){
            $(request.indf).text(request.likes)
            $("#" + request.basic_indf + '1234').load(location.href + ' ' + "#" + request.basic_indf + '1234');
        }
    });
});

$('.delete-single-comment').click(function(l){
    l.preventDefault()
    var single_delete_comment = $(this)
    var single_delete_commentURL = single_delete_comment.attr('href')

    $.ajax({
        url: single_delete_commentURL,
        method: '',
        data: {},
        success: function(request){
            $(request.basic_indf).remove();
        }
    });
});

$('.user-follow-btn').click(function(u){
    u.preventDefault()
    var follow_user = $(this)
    var follow_userURL = follow_user.attr('href')

    $.ajax({
        url: follow_userURL,
        method: '',
        data: {},
        success: function(request){
            $('#' + request.basic_indf + '123').text(request.profile_followers)
            $('#' + request.basic_indf + '321').text(request.profile_followings)
            $('#' + request.basic_indf + '456').text(request.profile_followers)
            $('#' + request.basic_indf + '654').text(request.profile_followings)
            $('#' + request.basic_indf).load(location.href + ' ' + '#' + request.basic_indf);
        }
    });
});