from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *


def customer(request):
    return render(request, 'customer_info.html')