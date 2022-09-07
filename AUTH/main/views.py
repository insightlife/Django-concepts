from django.shortcuts import render

from .form import data,logindata

from django.contrib import messages

from django.contrib import auth

def sign(request):
    if request.method=='POST':
        f=data(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,'account created successfully')
    else:
        f=data()
    return render(request,'home.html',{'fm':f})

def loginn(request):
    if request.method=='POST':
        g=auth.forms.AuthenticationForm(data=request.POST)
        if g.is_valid():
            uname=g.cleaned_data['username']
            upass=g.cleaned_data['password']
            user=auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return render(request,'ok.html')
    else:
            g=auth.forms.AuthenticationForm()
    return render(request,'fast.html',{'fm':g})
      
    
  