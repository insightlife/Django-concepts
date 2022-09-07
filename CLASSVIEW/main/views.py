from django.shortcuts import render
from django.views.generic.base import View
from . import formm
# Create your views here.
class home(View):
    def get(self,request):
        x="suman"
        fm=formm.data()
        return render(request,'home.html',{'x':x,'fm':fm})
    def post(self,request):
        return render(request,'homeo.html')
