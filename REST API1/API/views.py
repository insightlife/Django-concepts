import io
import requests
from functools import partial
from django.http.response import HttpResponse
from django.shortcuts import render
from requests.api import request
from rest_framework import serializers
from .models import Student
from .serializersd import studentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

@csrf_exempt
def main(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=studentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            stu=Student.objects.all()
            serializer=studentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json') 
    else:
        res = {'error':'error occured'}
        jsondata= JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")

@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            jsondata= JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type="application/json")
    else:
        res = {'error':'error occured'}
        jsondata= JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")

@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer= studentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated'}
            jsondata= JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type="application/json")
        else:
            res = {'error':'error is occured'}
            jsondata= JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type="application/json")   
    else:
        res = {'error':'error occured'}
        jsondata= JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")
@csrf_exempt
def delete_operation(request):
    if request.method == "DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}
        jsondata= JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")
    else:
        res = {'error':'error occured'}
        jsondata= JSONRenderer().render(res)
        return HttpResponse(jsondata,content_type="application/json")