$(document).ready(function(){
      // 무한 스크롤 - 스크롤 event
    $(window).scroll(function(){
        var scrollTop = $(window).scrollTop();
        var documentHeight = $(document).height();
        var windowHeight = $(window).height();

        if( scrollTop >= documentHeight - windowHeight){
            var timer;
            if (!timer) {
                timer = setTimeout(function(){
                    timer = null;
                    var page = $('#page').val();
                    callMorePostAjax(page);
                    $('#page').val(parseInt(page)+1);
                }, 500);
            }
        }
    });
});

// ----------------------------------- 무한 스크롤 관련  --------------------------------------

// 무한스크롤 script
 function callMorePostAjax(page) {
    $.ajax( {
    url: '/posts/more/',
    type : 'post',
    dataType: 'html',
    data: {
        page: page,
        csrfmiddlewaretoken: csrftoken
    },
    success: addMorePostAjax
    });
}

// 해당 id div tag에 내용을 append
function addMorePostAjax(data) {
    $('#post_list_ajax').append(data);
}
