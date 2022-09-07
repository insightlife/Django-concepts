from django.shortcuts import render

from django import http

from .formm import user_reg

def home(request):
    form=user_reg()
    return render(request,'home.html',{'form':form})

def login(request):
    return http.HttpResponse("thank you")