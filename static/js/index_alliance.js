$(function() {
    $("img.lazy").lazyload({　　　　　　　　　　
        effect: "fadeIn", //渐现，show(直接显示),fadeIn(淡入),slideDown(下拉)
        threshold: 100 //预加载，在图片距离屏幕180px时提前载入
        //event: 'click', // 事件触发时才加载，click(点击),mouseover(鼠标划过),sporty(运动的),默认为scroll（滑动）
        //failure_limit: 2 //加载2张可见区域外的图片,lazyload默认在找到第一张不在可见区域里的图片时则不再继续加载,但当HTML容器混乱的时候可能出现可见区域内图片并没加载出来的情况
    });
    $('.mySlideshow').edslider({
        width: 480,
        height: 300
    });

    // 跟随屏幕移动
    $(document).ready(function () {
        var menuYloc = 300;
        $(window).scroll(function () {
            var offsetTop = menuYloc + $(window).scrollTop() + "px";
            $("#top_text").animate({ top: offsetTop }, { duration: 600, queue: false });
        });
    });

    // 金蜘蛛奖 点击显示全部 展示全部参选作品
    $('.view_all').click(function(e) {
        sort_id = $('.view_all').attr("id");
        $.ajax({
            type: 'GET',
            url: '/all_award_cases/'+sort_id+'/',
            dataType: 'json',
            success: function(response){

                var data = response.list;
                var length = response.list.length;

                var result = '';
                /****业务逻辑块：实现拼接html内容并append到页面*********/
                for(var i=0; i<length; i++){
                    if(i%4 == 0){
                        result += '<tr>'
                    }
                    result +='<td>' +
                        '<div class="back_img"><img style="width:240px;height:360px;" src="/media/'+data[i].fields.image+'"><div class="text_flow_img">' +
                        '<span>'+data[i].fields.title+'</span></div><div class="poll_text"><span id="poll_num-'+data[i].fields.id+'" style="color:red;">' +
                    data[i].fields.fav_nums + '</span><a href="javascript:void(0);"><img id="'+data[i].fields.id+'" class="poll" src="/static/images/poll.png"></a></div></div>'
                        + '</td>';
                    if(i%4 == 0){
                        result += '</tr>'
                    }
                }
                $('.award_table').append(result);
                /*******************************************/

                /*隐藏more按钮*/
                $(".view_all").hide();
            },
            error: function(xhr, type){
                alert('服务器异常!');
            }
    });
    });

    // 金蜘蛛奖参赛作品点赞
    $('.poll').click(function(e) {
        var iterm_id = $(this).attr("id");
        $.ajax({
            type: 'GET',
            url: '/poll/'+iterm_id+'/',
            dataType: 'json',
            success: function(response){
                var msg = response['msg'];
                if(msg == 'fail') {
                    alert('您已投票过!');
                } else {
                    var id = 'poll_num-'+iterm_id;
                    $('#'+id).html(parseInt($('#'+id).text())+1);
                }
            },
            error: function(xhr, type){
                alert('服务器异常!');
            }
    });
    });

    // 金蜘蛛奖 点击显示全部往期回顾
    $('.view_all_history').click(function(e) {
        $.ajax({
            type: 'GET',
            url: '/all_award_history/',
            dataType: 'json',
            success: function(response){

                var data = response.list;
                var length = response.list.length;

                var result = '';
                /****业务逻辑块：实现拼接html内容并append到页面*********/
                for(var i=0; i<length; i++){
                    result +='<li><a href="'+data[i].fields.id+'" target="_blank"><span class="spider_text">'+data[i].fields.title+'</span></a></li>'
                }
                $('.history_ul').append(result);
                /*******************************************/

                /*隐藏more按钮*/
                $(".view_all_history").hide();
            },
            error: function(xhr, type){
                alert('服务器异常!');
            }
    });
    });
});
