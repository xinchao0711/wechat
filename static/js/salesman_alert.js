function to_customer(employee_openid) {
    //获取该业务员的openid
    
    window.location.href = "/aiins/employee_manange/customer_list?employee_openid="+employee_openid;
    /**
    $.ajax({
        url: '/aiins/employee_manange/customer_list/',
        type: 'post',
        dataType: 'json',
        data: {
            employee_openid: employee_openid
        },
        success:function(response){
            alert(response);
        },
        error:function(){
            alert("出错！");
        }
    });
    //window.location.href = "/aiins/customer_list/";
     */
}

function about_customer(obj){
    var openid = obj.id;
    window.location.href = "/aiins/user/find_one?openid="+openid;
}