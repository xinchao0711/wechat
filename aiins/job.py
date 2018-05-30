from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
from aiins import models


# Create your views here.
def sendData(request):
    job = request.GET.get("job",None)
    salary = request.GET.get("salary",None)
    medicare = request.GET.get("medicare",None)
    
    request.session["user_dict"]["job"] = job
    request.session["user_dict"]["salary"] = salary
    request.session["user_dict"]["medicare"] = medicare
    
    request.session["job"] = job
    userinfo =  request.session["user_dict"]
    
    #models.User.objects.create(**userinfo)
    return render(request, 'health.html', {"data": request.session["user_dict"]})