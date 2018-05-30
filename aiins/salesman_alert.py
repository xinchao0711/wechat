from __future__ import unicode_literals
from django.shortcuts import render
from django.http import *
from aiins import models
import json
import datetime
import urllib2


def salesman_index(request):
    
    
    
    code = request.GET.get("code", None)
    user_num = 0
    
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
        employee = models.Employee.objects.filter(openid=openid)
        if employee:
            user_list = models.User.objects.filter(employee = openid)
            user_num = len(user_list)
        else:
            models.Employee.objects.create(nickname=nickname, openid=openid)
            user_num = 0
           
    
    return render(request, 'salesman_alert.html',{"user_num":user_num, "openid":openid,"code":code})

def find_customer_by_employeeid(request):
    employee_openid = request.GET.get("employee_openid")
    customers = models.User.objects.filter(employee=employee_openid)
    for item in customers:
        birth_year = int(item.birthday[0:4])
        now_year = datetime.datetime.now().year
        age = int(now_year) - birth_year
        item.birthday = age
#    customers_json = serializers.serialize("json", customers)
#    print(customers_json)
    return render(request, 'customers_list.html', {"customers": customers})