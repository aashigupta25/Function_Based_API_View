from functools import partial
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person_api(request, pk = None):
    if request.method =='GET':
        id = pk
        if id is not None:
            per = Person.objects.get(id= id)
            serializer = PersonSerializer(per)
            return Response(serializer.data)
        per = Person.objects.all()
        serializer = PersonSerializer(per, many= True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = PersonSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'}, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = pk
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        id = pk
        per = Person.objects.get(pk= id)
        per.delete()
        return Response({'msg':'data deleted'})




