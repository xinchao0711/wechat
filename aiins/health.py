from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
# Create your views here.


def sendData(request):
    height = request.GET.get("height",None)
    weight = request.GET.get("weight",None)
    bmi = request.GET.get("bmi",None)
    steps = request.GET.get("steps",None)
    
    
    request.session["user_dict"]["height"] = height
    request.session["user_dict"]["weight"] = weight
    request.session["user_dict"]["bmi"] = bmi
    request.session["user_dict"]["steps"] = steps
    
    print()
    request.session["weight"] = weight
    
    r =  request.session["user_dict"]["steps"]
    return render(request, 'family_struct.html', {"data":  request.session["user_dict"]})