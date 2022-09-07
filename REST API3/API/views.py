from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .seraliizer import studentSeralizier
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

@api_view(['GET','POST','PUT','DELETE'])
def hello_world(request):
    if request.method == "GET":
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=studentSeralizier(stu)
            return Response(serializer.data)
        else:
            stu=Student.objects.all()
            serializer=studentSeralizier(stu,many=True)
            return Response(serializer.data) 
    if request.method == "POST":
        serializer= studentSeralizier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'POST request'})
        else:
            return Response(serializer.errors)
    if request.method == "PUT":
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=studentSeralizier(stu,data = request.data,partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'PUT request'})
            else:
                return Response(serializer.errors)
    if request.method == "PUT":
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'DELETE request'})

