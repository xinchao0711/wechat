from __future__ import unicode_literals
from django.shortcuts import render
from models import Employee
from django.http import *
# Create your views here.
def family_rec(request):
    return render(request, 'family_security_rec.html')

def children_rec(request):
    return render(request, 'children_rec.html')

def health_rec(request):
    return render(request, 'health_rec.html')

def travel_rec(request):
    return render(request, 'travel_rec.html')

def more_rec(request):
    return render(request, 'children_rec.html')