from django.shortcuts import render

from django.contrib import sessions 

def set(request):
    request.session['name']="akash"
    return render(request,'set.html')

def get(request):
    x=request.session['name']
    return render(request,'get.html',{'x':x})

def function(request):
    y=request.session.keys()
    p=request.session.items()
    c=request.session.setdefault('age','26')
    return render(request,'fun.html',{'y':y,'p':p,'c':c})