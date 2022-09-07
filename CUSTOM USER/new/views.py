from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import customuser
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import login_form,name_form,password_form,user_change_form,account_creation_form
# Create your views here.
def signup(request):
    if request.method == "POST":
        fm = account_creation_form(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'account.html')
        else:
            fm = account_creation_form()
            messages.success(request,'username is already exists')
            return render(request, "signup.html", {'fm':fm})
    else:
        fm = account_creation_form()
        return render(request,'signup.html',{'fm':fm})

def login(request):
    if request.method == 'POST':
        user_fm = login_form(data=request.POST)
        if user_fm.is_valid():
            uname = user_fm.cleaned_data['username']
            upass = user_fm.cleaned_data['password']
            user = auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('account')
            else:
                user_fm = login_form()
                messages.success(request,'username or password is invalid')
                return render(request, "login.html", {'fm':user_fm})
        else:
            user_fm = login_form()
            messages.success(request,'username and password does not match')
            return render(request, "login.html", {'fm':user_fm})
    else:
        user_fm = login_form()
        return render(request,'login.html',{'fm':user_fm})

def account(request):
    if request.user.is_authenticated:
        user_acc = user_change_form(instance=request.user)
        return render(request,'account_detail.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')

def password(request):
    if request.method == "POST":
        fm = password_form(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('login')
        else:
            fm = password_form(request.user)
            return render(request,'password.html',{'fm':fm})
    else:
        fm = password_form(request.user)
        return render(request,'password.html',{'fm':fm})

def editaccount(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = user_change_form(request.POST,instance=request.user)
            if user.is_valid():
                user.save()
                return HttpResponseRedirect('login')
            else:
                user_acc = user_change_form(instance=request.user)
                return render(request,'master/editprofile.html',{'data':user_acc})
        else:
            user_acc = user_change_form(instance=request.user)
            return render(request,'master/editprofile.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')

def passwordchange(request):
    if request.method == "POST":
        fm = name_form(data=request.POST)
        if fm.is_valid():
            upass = fm.cleaned_data['name']
            v=User.objects.get(username=upass)
            if v:
                return HttpResponseRedirect('password')
            else:
                return render(request,'master/ok.html')
        else:
            return render(request,'master/ok.html')
    else:
        fm = name_form()
        return render(request,'master/resetpassword.html',{'fm':fm})

def set_date(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user_acc = user_change_form(instance=request.user)
            return render(request,'account_detail.html',{'data':user_acc})
    else:
        date_ = request.POST['concern']
        print(date_)
        print(type(date_))
        k= date_.split('T')
        print(k)
        x= customuser(user_name=request.user,slottime=date_,slotdate=k[0])
        x.save()
        return render(request,'home.html')    
import pywhatkit

def home(request):
    if request.method == "GET":
        return render(request,'home.html')
    else:
        date_ = request.POST['concern']
        print(date_)
        d= User.objects.get(username="suman9")
        print(d)
        b = customuser.objects.filter(user_name=d)
        print(b)
        n= list(b)
        print(n)
        return render(request,'home.html')

def choose(request):
    if request.method == "GET":
        return render(request,'choice.html')
    else:
        date_ = request.POST['concern']
        print(date_)
        print(type(date_))
        k= date_.split('T')
        print(k)
        d= customuser.objects.filter(ekdate=k[0])
        print(d)
        return render(request,'choice.html')