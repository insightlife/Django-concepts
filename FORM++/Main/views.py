from django.shortcuts import render

from django.http import HttpResponseRedirect

from . import form_user

def home(request):
    form=form_user.user()
    return render(request,'header.html',{'form':form})

def response(request):
    if request.method=='GET':
        users=form_user.user(request.GET)
        if users.is_valid():
             print("form is validated")
             print(users.cleaned_data['name'])
             return HttpResponseRedirect('/hello')
        else:
            print("form is invalid")
    else:
        form=form_user.user()
        return render(request,'header.html',{'form':form})

def thanks(request):
    return render(request,'thank.html')

        