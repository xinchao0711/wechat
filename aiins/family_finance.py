from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
# Create your views here.
def sendData(request):
    asset = request.GET.get('asset')
    income = request.GET.get('income')
    
    request.session["user_dict"]["asset"] = asset
    request.session["user_dict"]["income"] = income
    
    request.session["asset"] = asset
    
    
    return render(request, 'travel.html', {"data": str( request.session["user_dict"])})