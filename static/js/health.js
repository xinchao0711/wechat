function cal_bmi(){
    var height = $('#height').val();
    var weight = $('#weight').val();
    var bmi = (parseInt(weight)/(Math.pow(parseInt(height)/100,2))).toFixed(1);
    $('#bmi').val(bmi);
}

function health_next(){
    var int_height = parseInt($('#height').val());
    var int_weight = parseInt($('#weight').val());
    var int_bmi = parseInt($('#bmi').val());
    var int_step_num = parseInt($('#step_num').val());
    

    window.location.href = '/aiins/health/senddata?height='+int_height+'&weight='+int_weight+'&bmi='+int_bmi+'&steps='+int_step_num;
	/**
    $.ajax({
        url: '/aiins/family_struct/senddata',
        type: 'post',
        dataType: 'json',
        data: {
            height: int_height,
            weight: int_weight,
            bmi: int_bmi,
            step_num: int_step_num
        },
        success:function(response){
            if(response == '1'){
                window.location.href = "/aiins/family_struct/";//跳转到下一个页面
            }
        },
        error:function(){
            alert("出错！");
        }
    });
	*/
}
