from django.http.response import HttpResponse
from django.shortcuts import render
from .models import user
from .form import user_form
# Create your views here.
from django.contrib import messages
def regi(request):
    if request.method == "POST":
        fm=user_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,"your account has been created")
    else:
        print("error")
        fm=user_form()
    return render(request,'home.html',{'form':fm})