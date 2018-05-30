from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Employee(models.Model):
    nickname = models.CharField(max_length=50,null=True,blank=True)
    openid =  models.CharField(max_length=50,null=True,blank=True)
    name =  models.CharField(max_length=50,null=True,blank=True)
    
    
    
    
class User(models.Model):
    openid =  models.CharField(max_length=50,null=True,blank=True)
    nickname = models.CharField(max_length=20,null=True,blank=True)
    sex = models.CharField(max_length=10,null=True,blank=True)
    birthday = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=10,null=True,blank=True)
    job = models.CharField(max_length=20,null=True,blank=True)
    salary = models.CharField(max_length=20,null=True,blank=True)
    medicare = models.CharField(max_length=20,null=True,blank=True)
    height = models.CharField(max_length=20,null=True,blank=True)
    weight = models.CharField(max_length=20,null=True,blank=True)
    bmi = models.CharField(max_length=20,null=True,blank=True)
    steps = models.CharField(max_length=20,null=True,blank=True)
    family = models.CharField(max_length=20,null=True,blank=True)
    asset = models.CharField(max_length=20,null=True,blank=True)
    income = models.CharField(max_length=50,null=True,blank=True)
    travel = models.CharField(max_length=20,null=True,blank=True)
    employee =  models.CharField(max_length=20,null=True,blank=True)
    name = models.CharField(max_length=20,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=20,null=True,blank=True)
    product = models.CharField(max_length=20,null=True,blank=True)
    question = models.CharField(max_length=500,null=True,blank=True)
    buyins = models.CharField(max_length=20,null=True,blank=True)
    remark = models.CharField(max_length=100,null=True,blank=True)
    