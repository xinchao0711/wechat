from __future__ import unicode_literals
from django.shortcuts import render
#from models import Employee
from aiins import models
from django.http import *
# Create your views here.
def sendData(request):
    
    request.session["user_dict"]["travel"] = request.GET.get("travel")
    
    openid = request.session["user_dict"]["openid"]
    
    userinfo = dict(request.session["user_dict"])
    user = models.User.objects.filter(openid=openid)
    if user:
         models.User.objects.filter(openid=openid).update(**userinfo)
            
    else:
        models.User.objects.create(**userinfo)
    return render(request, 'result.html')
