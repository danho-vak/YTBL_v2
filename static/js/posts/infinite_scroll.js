$(document).ready(function(){
      // 무한 스크롤 - 스크롤 event
    $(window).scroll(function(){
        var scrollTop = $(window).scrollTop();
        var documentHeight = $(document).height();
        var windowHeight = $(window).height();


        if( scrollTop >= documentHeight - windowHeight){
            var end_of_page_num = parseInt($('#end_of_page_num').val())
            var current_page_num = parseInt($('#page').val())
            $('#page').val(current_page_num+1);

            var timer;
            if (!timer) {
                timer = setTimeout(function(){
                    timer = null;
                    if ((current_page_num > 1) && (current_page_num <= end_of_page_num)) {
                        callMorePostAjax(current_page_num);
                    }
                }, 500);
            }
        }
    });
});

// ----------------------------------- 무한 스크롤 관련  --------------------------------------

// 무한스크롤 script
 function callMorePostAjax(page) {
    $.ajax( {
    url: '/posts/',
    type : 'get',
    dataType: 'html',
    data: {
        page: page,
    },
    success: addMorePostAjax
    });
}

// 해당 id div tag에 내용을 append
function addMorePostAjax(data) {
    $('#post_list_ajax').append(data);
}
