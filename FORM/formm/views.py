from django.shortcuts import render

from formm.form import student

from formm.models import student_no

def index(request):
    return render(request,'index.html')

def student_info(request):
    form=student()
    return render(request,'app.html',{'form':form})

def kit(request):
    if request.method == 'POST':
        form= student(request.POST)
        if form.is_valid():
            x=form.cleaned_data['name']
            y=form.cleaned_data['email']
            print(x,y)
            s = student_no(id=x,email=y)
            s.save()
    return render(request,'index.html',{'x':x,'y':y})





