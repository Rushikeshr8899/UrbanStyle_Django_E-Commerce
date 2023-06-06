from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from .models import *

# Create your views here.
# def Register(request):
#     error=False
#     if request.method=="POST":
#         first_name=request.POST['first_name']
#         username=request.POST['username']
#         email=request.POST['email']
#         city=request.POST['city']
#         country=request.POST['country']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         user=User.objects.create_user(first_name=first_name,username=username,email=email,password1=password1,password2=password2)
#         Register.objects.create(user=user,city=city,country=country)
#         error=True
#
#     return render(request,'Register.html',{'a':error})
