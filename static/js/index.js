function chooseman(){
    $('#man_icon').css('border','2px solid grey');
    $('#man_icon').css('opacity','0.5');
    $('#woman_icon').css('border','none');
    $('#woman_icon').css('opacity','1');

}

function choosewoman(){
    $('#woman_icon').css('border','2px solid grey');
    $('#woman_icon').css('opacity','0.5');
    $('#man_icon').css('border','none');
    $('#man_icon').css('opacity','1');

}

function index_next(){
    //获取性别
    var sex;
    var man = $('#man_icon').css('opacity');
    var woman = $('#woman_icon').css('opacity');
    if ((man == '0.5') || (woman == '0.5')) {
        if (man == '0.5') {
            sex = 'man';
        } else {
            sex = 'woman';
        }
    } else {
        alert('请选择性别！');
        return;
    }
    //获取出生日期
    var birth_date = $('#birth_date').val();
    //alert(birth_date);
    //获取居住地
    var city = $("#place option:selected").text();
    //alert(place);
    
    /*
    $.ajax({
        url: '/aiins/user/find_one',
        type: 'post',
        dataType: 'json',
        data: {
            openid: 'ob1eH1fAx8P8AhgizJw7V00LUTUA'
        },
        success:function(response){
            alert(response.nickname);
        },
        error:function(){
            alert("出错！");
        }
    });
    
    */
    
	window.location.href = '/aiins/index/senddata?sex='+sex+'&birthday='+birth_date+'&city='+city;
    //向服务器提交数据
	
    
	

}