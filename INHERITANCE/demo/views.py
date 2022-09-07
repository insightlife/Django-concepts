from http.client import HTTPResponse
from re import S
import string
from django.shortcuts import render
from .models import MyPerson, fooball,student
from django.http import HttpResponse
from django.views import View
from .form import shine
# Create your views here.
def home(request):
    p= student();
    p.firstname="suman"
    p.lastname="patra"
    p.save()
    print(p)
    print(p.fullName())
    return HttpResponse('result coming')

class demon(View):
    def get(self, request):
        return HttpResponse('result')

class holy(View):
    def get(self,request):
        f= shine();
        return render(request,'holy.html',{'f':f})

    def post(self,request):
        f=shine(request.POST)
        if f.is_valid():
            f= fooball.objects.create(name=f.cleaned_data['name'])
            self.ghost(request)
            return HttpResponse('form saved')
        else:
            return HttpResponse('something wrong')

    def ghost(self,request):
        print("hello")

def chitt(request,templatename):
    print(templatename);
    return HttpResponse('popoo');

class chit(View):
    template=''
    def get(self,request):
        print(self.template)
        return render(request,'basic.html')