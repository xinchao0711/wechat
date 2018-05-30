from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
# Create your views here.


def sendData(request):
    family = request.GET.get("family", None)
    request.session["user_dict"]["family"] = family
    
    request.session["family"] = family
    
    #r =  request.session["user_dict"]["weight"]
    return render(request, 'family_finance.html', {"data": str( request.session["user_dict"])})