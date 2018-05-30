from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import *
from aiins import models
import json
import datetime


def salesman_index(request):
    
    
    
    code = request.GET.get("code", None)
    if code != None:
        get_access_token_url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=wxa8cd5ba2da901ad6&secret=299d2cfee30284608010ff872e040ecf&code="+ code +"&grant_type=authorization_code"
        f1 = urllib2.urlopen(get_access_token_url)
        data = dict(json.loads(f1.read()))
        access_token = data["access_token"]
        openid = data["openid"]
        
        get_userinfo_url = "https://api.weixin.qq.com/sns/userinfo?access_token=" + access_token + "&openid=" + openid + "&lang=zh_CN"
        testurl = "https://api.weixin.qq.com/sns/auth?access_token="+access_token+"&openid="+openid
        f2 = urllib2.urlopen(get_userinfo_url)
        
        userinfo = dict(json.loads(f2.read()))
        
        nickname = userinfo["nickname"]
    
    return render(request, 'salesman_alert.html')

def find_all_employee(request):
    employee_list = models.Employee.objects.all()
    employee_json_list = serializers.serialize("json", employee_list)
    return HttpResponse(employee_json_list, content_type='json')

    #customers_json = serializers.serialize("json", customers)
    #print(customers_json)
    #return render(request, 'customers_list.html', {"customers": customers})