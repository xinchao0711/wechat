function selectone(obj){
    var items = ["sig_nokid", "sig_kid", "mar_nokid", "mar_kid"];
    for(var i=0;i<items.length;i++){
        if(obj.id == items[i]){
            $("#"+items[i]).css('border','3px solid red');
            select_one = i;
        }else{
            $("#"+items[i]).css('border','none');
        }
    }
}

function family_struct_next() {
    window.location.href = '/aiins/family_struct/senddata?family='+select_one;
	/**
    $.ajax({
        url: '/aiins/family_struct/senddata',
        type: 'post',
        dataType: 'json',
        data: {
            family_struct: select_one
        },
        success:function(response){
            if(response == '1'){
                window.location.href = "/aiins/family_finance/";//跳转到下一个页面
            }
        },
        error:function(){
            alert("出错！");
        }
    });
	*/
}