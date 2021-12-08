from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Curso 
from .serializer import CursoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def curso_list(request):
    if request.method == 'GET' :
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos,many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        #Verificar si el serializador es valido
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def curso_detalle(request,pk):
    try:
        curso = Curso.objects.get(pk=pk)
    except Curso.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        serializer = CursoSerializer(curso) 
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CursoSerializer(curso,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

            