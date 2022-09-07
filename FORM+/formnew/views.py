from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from django.http import HttpResponse

from django.shortcuts import render

from formnew.form import student

def login(request):
    op=student()
    return render(request, 'name.html', {'form':op})

def sup(request):
    if request.method == 'POST':
        form = student(request.POST)
        if form.is_valid():
            username=form.cleaned_data['name']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
        else:
            pass

    userrss=authenticate(username='sovan',password='sovan123@')
    if userrss is None:
        return HttpResponse("not ok")

    else:
        return HttpResponse("ok")

