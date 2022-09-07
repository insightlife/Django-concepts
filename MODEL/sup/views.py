from django.shortcuts import render

from sup.models import info

def index(request):
    p=info(name='suman',age=23)
    p.save()
    return render(request,'index.html')