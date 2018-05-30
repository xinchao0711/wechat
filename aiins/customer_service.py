from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, Http404, HttpResponse, render_to_response
from aiins import models
from django.http import *
import json
import urllib2
from django.forms.models import model_to_dict
import datetime

# Create your views here.
def index(request):
    openid = request.GET.get("openid")
    
    user = models.User.objects.get(openid=openid)
    birth_year = int(user.birthday[0:4])
    now_year = datetime.datetime.now().year
    age = int(now_year)-birth_year
    user.birthday = age
    if user == None:
        r = '0';
    else:
        user_dict = model_to_dict(user)
    employees = models.Employee.objects.all()
    #return HttpResponse(json.dumps(user_dict))
    return render_to_response('customer_service_pc.html', locals())

def login(request):
    return render(request, "login.html")


def submit_data(request):
    
    return;