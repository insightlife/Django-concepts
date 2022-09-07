from django.shortcuts import render

# Create your views here.
def home(request):
    emp='suman'
    info={'id1':['suman','sovan','kalia'],'id2':['soubhagya','maliya','lalita']}
    stu={'stu1':{'name':'suman','rollno':23},'stu2':{'name':'sovan','rollno':26},'stu3':{'name':'sovan','rollno':26}}
    return render(request,'home.html',{'student':stu,'employee':emp,'info':info})