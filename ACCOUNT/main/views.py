from django.shortcuts import render

from django.contrib.auth import forms,update_session_auth_hash

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from .forms_user import data,data_up

from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def user_signup(request):
    if request.method=='POST':
        f=data(request.POST)
        if f.is_valid():
            f.save()
    else:
        f=data()
    return render(request,'home.html',{'fm':f})

def user_login(request):
        if request.method=='POST':
            f=forms.AuthenticationForm(request=request,data=request.POST)
            if f.is_valid():
                uname=f.cleaned_data['username']
                upass=f.cleaned_data['password']
                userk=authenticate(username=uname,password=upass)
                if userk is not None:
                    login(request,userk)
                    return HttpResponseRedirect('/profile')
        else:
            f=forms.AuthenticationForm()
            return render(request,'homeo.html',{'fm':f})   

def user_profile(request):
    if request.user.is_authenticated:
        su=data_up(instance=request.user)
        return render(request,'home2.html',{'user':request.user,'su':su})
    else:
        return HttpResponseRedirect('/login')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def changepass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            k=forms.PasswordChangeForm(user=request.user,data=request.POST)
            if k.is_valid():
                update_session_auth_hash(request,k.user)
                k.save()
                return HttpResponseRedirect('/profile')
        else:
            k=forms.PasswordChangeForm(user=request.user)
            return render(request,'home3.html',{'fm':k})
    else:
        return HttpResponseRedirect('/login')

