from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from aiins import models
from django.http import *
import json
import urllib2
from django.forms.models import model_to_dict
import datetime


# Create your views here.
def findAll(request):
    user_list = models.User.objects.all()
    
    return render(request,"user_list.html", {"user_list":user_list})


def findById(request):
    if request.method == 'POST':
        openid = request.POST.get("openid")
        user = models.User.objects.get(openid=openid)
        if user == None:
            r = '0';
        else:
            user_dict =  model_to_dict(user)
        return HttpResponse(json.dumps(user_dict))
    else:
        openid = request.GET.get("openid")
        user = models.User.objects.get(openid=openid)
        birth_year = int(user.birthday[0:4])
        now_year = datetime.datetime.now().year
        age = int(now_year)-birth_year
        user.birthday = age
        return render_to_response("customer_info.html", locals())


def findByEmp(request):
    
    employee = request.User.get("employee")
    
    user_list = models.User.objects.get(employee = employee)
    
    return HttpResponse(user_list)