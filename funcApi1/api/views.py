from functools import partial
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person_api(request):
    if request.method =='GET':
        id = request.data.get('id')
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
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        per = Person.objects.get(pk = id)
        serializer = PersonSerializer(per, data = request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return response(serializer.errors)

    if request.method == 'DELETE':
        id = request.data.get('id')
        per = Person.objects.get(pk= id)
        per.delete()
        return Response({'msg':'data deleted'})




