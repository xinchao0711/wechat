from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from aiins import models
from django.http import *
import json
import urllib2


# Create your views here.
def updateInfo(request):
 
    name = request.GET.get("name")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    question = request.GET.get("question")
    buyins = request.GET.get("buyins")
    remark = request.GET.get("remark")
    openid = request.GET.get("openid")
    models.User.objects.filter(openid=openid).update(name=name, phone=phone, email=email, question=question, buyins=buyins, remark=remark)
    
    return HttpResponse("success")


def updateEmployee(request):
    employee = request.GET.get("employee")
    openid = request.GET.get("openid")
    
    models.User.objects.filter(openid=openid).update(employee=employee)
    return HttpResponse("success")