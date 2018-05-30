from __future__ import unicode_literals
from django.shortcuts import render
from aiins import models
from django.http import *
import json
import urllib2


# Create your views here.
def index(request):
    
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
        user_dict = dict()
        request.session["user_dict"] = user_dict
        request.session["user_dict"]["nickname"] = nickname
        request.session["user_dict"]["openid"] = openid
        
        #models.Employee.objects.create(openid=openid, nickname=nickname)
        
    
    
    
    """
    #models.User.objects.create(openid=openid, nickname=nickname)
    #request.session["openid"] = openid
    #request.session["nickname"] = nickname
   
    #return render(request, 'index.html',{"openid":openid,"nickname":nickname})
    
    """
    return render(request, 'index.html')



def index1(request):
    ans0 = {'head': 'hello world'}
    return render(request, 'firstpage.html', ans0)

def job(request):
    return render(request, 'job.html')
def health(request):
    return render(request, 'health.html')
def family_struct(request):
    return render(request, 'family_struct.html')
def family_finance(request):
    return render(request, 'family_finance.html')
def travel(request):
    return render(request, 'travel.html')