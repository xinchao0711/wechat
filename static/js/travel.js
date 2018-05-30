function travel_sel(obj){
    for(var i = 0; i<3; i++){
        if(obj.id == ('travel_'+i)){
            //添加背景色
            $("#travel_"+i).css('background-color','grey');
            freq = i;
        }else{
            $("#travel_"+i).css('background-color','white');
        }
    }
}

function travel_next(){
    //alert(freq);
    //向服务器提交数据
    window.location.href = "/aiins/travel/senddata?travel=" + freq;
    /**
    $.ajax({
        url: '/aiins/travel/senddata',
        type: 'post',
        dataType: 'json',
        data: {
            freq: freq
        },
        success:function(response){

        },
        error:function(){
            alert("出错！");
        }
    });
     */
}