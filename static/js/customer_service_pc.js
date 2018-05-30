function set_employee(user_openid){
    var employee_openid = $('#employee_select').val();
    //alert(employee_openid);
    
    
    $.ajax({
        url: '/aiins/customer_service_pc/set_employee',
        type: 'get',
        dataType: 'text',
        data: {
            openid: user_openid,
            employee: employee_openid
        },
        success:function(response){
            alert("分配成功！");

        },
        error:function(){
            alert("出错！");
        }
    });
        
}

function get_form_data(){
    var name = $('#name').val();
    var sex =  $('input:radio[name="sex_select"]:checked').val();
    var phone = $('#phone').val();
    var email = $('#email').val();
    var buyins = $('input:checkbox[name="buyins"]:checked').val();
    var product = $('#product').val();
    var question = $('#question').val();
    var remark = $('#remark').val();
    var openid = 'ob1eH1fAx8P8AhgizJw7V00LUTUA';

    $.ajax({
        url: '/aiins/customer_service_pc/submitData',
        type: 'get',
        dataType: 'text',
        data: {
            name: name,
            sex: sex,
            phone: phone,
            email: email,
            buyins: buyins,
            product: product,
            question: question,
            remark: remark,
            openid: openid
        },
        success:function(response){
            alert("保存成功！");

        },
        error:function(){
            alert("出错！");
        }
    });
}