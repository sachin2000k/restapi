from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt     #for csrf
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializer import employeesSerializer
import json
from rest_framework.parsers import JSONParser

@csrf_exempt                 #problem
def load_employee(request):

    if request.method=='POST':
        data=JSONParser().parse(request)
        serial=employeesSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return JsonResponse(serial.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        result = []
        employee1 = employees.objects.all()
        serial = employeesSerializer(employee1, many=True)
        return JsonResponse(serial.data, safe=False)

@csrf_exempt
def load_detail(request, username):

    try:
        emp1 = employees.objects.get(username=username)
    except employees.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = employeesSerializer(emp1)
        return JsonResponse(serializer.data)







'''
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = employeesSerializer(emp1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        emp1.delete()
        return HttpResponse(status=204)
'''