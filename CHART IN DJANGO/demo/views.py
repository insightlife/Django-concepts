from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
    label=[]
    data =[]
    s=student.objects.all()
    for i in s:
        label.append(i.name)
        data.append(i.age)
    return render(request,'main.html',{'data':data,'label':label})