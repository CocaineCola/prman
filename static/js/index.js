$(function() {
    $("img.lazy").lazyload({　　　　　　　　　　
        effect: "fadeIn", //渐现，show(直接显示),fadeIn(淡入),slideDown(下拉)
        threshold: 100 //预加载，在图片距离屏幕180px时提前载入
        //event: 'click', // 事件触发时才加载，click(点击),mouseover(鼠标划过),sporty(运动的),默认为scroll（滑动）
        //failure_limit: 2 //加载2张可见区域外的图片,lazyload默认在找到第一张不在可见区域里的图片时则不再继续加载,但当HTML容器混乱的时候可能出现可见区域内图片并没加载出来的情况
    });
    $('.mySlideshow').edslider({
        width: '100%',
        height: 500
    });
    $(window).scroll(function() {
        if ($(".navbar").offset().top > 50) {
            $(".navbar").addClass("top-nav");
        } else {
            $(".navbar").removeClass("top-nav");
        }
    });
    // 手机端使用
    $('#showMenu').click(function() {
        var display = $('.menu ul').css('display');
        if (display == 'none') {
            $('.menu ul').css('display', 'block');
        } else {
            $('.menu ul').css('display', 'none');
        }
    });
    $('.menu ul li a').click(function(e) {
        $('.menu ul').css('display', 'none');
    });

    // 我们的案例 点击MORE加载新的20个案例
    var page = 1;    /*计数器*/
    $('.more').click(function(e) {
        page = page + 1;
        $.ajax({
            type: 'GET',
            url: '/more_cases/'+page+'/',
            dataType: 'json',
            success: function(response){

                var data = response.list;
                var length = response.list.length;

                var result = '<tr>';
                /****业务逻辑块：实现拼接html内容并append到页面*********/
                for(var i=0; i<length; i++){
                    result +='<td><a href="/article_detail/'+ data[i].pk +'"><img src="/media/'+ data[i].fields.image +'"></a></td>';
                }
                result += '</tr>';
                $('.cases').append(result);
                /*******************************************/

                /*隐藏more按钮*/
                if (response.msg == 'fail'){
                    $(".more").hide();
                } else {
                    $(".more").show();
                }
            },
            error: function(xhr, type){
                alert('服务器异常!');
            }
    });
    });
});
