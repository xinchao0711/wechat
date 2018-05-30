function family_finance_next() {
    var income = $('#income option:selected').text();
    var property = $("input:checkbox:checked").map(function(index,elem) {
            return $(elem).val();
        }).get().join(',');
    //alert(income+property);
    //向服务器提交数据
    
    
    
    
    window.location.href = '/aiins/family_finance/senddata?income='+income+'&asset='+property;
	/**
    $.ajax({
        url: '/aiins/family_finance/senddata',
        type: 'post',
        dataType: 'json',
        data: {
            income: income,
            property: property
        },
        success:function(response){
            if(response == '1'){
                window.location.href = "/aiins/travel/";//跳转到下一个页面
            }
        },
        error:function(){
            alert("出错！");
        }
    });
	*/
}