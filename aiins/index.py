from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
# Create your views here.


def sendData(request):
    
    sex = request.GET.get("sex",None)
    city = request.GET.get("city",None)
    birthday = request.GET.get("birthday",None)
    request.session["user_dict"]["sex"] = sex
    request.session["user_dict"]["city"] = city
    request.session["user_dict"]["birthday"] = birthday
    
    request.session["sex"] = sex
    
    return render(request, 'job.html', {"data": str(request.session["user_dict"])})