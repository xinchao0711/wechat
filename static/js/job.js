function job_next(){
    //获取工作类型
    var job_type = $('#job_type option:selected').text();
    //获取年薪
    var salary = $('#salary option:selected').text();
    //获取是否有社会医疗保险
    var medicare = $("input[type='radio']:checked").val();
    //alert(job_type + salary + medicare);

    window.location.href = '/aiins/job/senddata?salary='+salary+'&job='+job_type+'&medicare='+medicare;
	/**
    $.ajax({
        url: '/aiins/job/senddata',
        type: 'post',
        dataType: 'json',
        data: {
            job_type: job_type,
            salary: salary,
            medicare: medicare
        },
        success:function(response){
            if(response == '1'){
                window.location.href = "/aiins/health/";//跳转到下一个页面
            }
        },
        error:function(){
            alert("出错！");
        }
    });
	*/
}

function job_prev() {
    //window.location.href = document.referrer;
	window.location.href = window.history.back();
}