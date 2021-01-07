from rest_framework import viewsets
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer, PublicacionSerializers, ComentarioSerializers
from Apps.usuario.models import Usuario, Publicacion, Comentario


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializers

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset= Comentario.objects.all()
    serializer_class= ComentarioSerializers


@api_view(['GET', 'POST', 'DELETE'])
def usuario_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all 
    if request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UserSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse(usuario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def publicacion_list(request): 
    if request.method == 'POST':
        publicacion_data = JSONParser().parse(request)
        publicacion_serializer = PublicacionSerializers(data=publicacion_data)
        if publicacion_serializer.is_valid():
            publicacion_serializer.save()
            return JsonResponse(publicacion_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(publicacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def comentario_list(request):
     if request.method == 'POST':
        comentario_data = JSONParser().parse(request)
        comentario_serializer = ComentarioSerializers(data=comentario_data)
        if comentario_serializer.is_valid():
            comentario_serializer.save()
            return JsonResponse(comentario_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comentario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def usuario_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        usuario = Usuario.objects.get(pk=pk) 
    except usuario.DoesNotExist: 
        return JsonResponse({'message': 'Este usuario no existe'}, status=status.HTTP_404_NOT_FOUND)

def publicacion_detail(request, pk):
    try: 
        publicacion = Publicacion.objects.get(pk=pk) 
    except publicacion.DoesNotExist: 
        return JsonResponse({'message': 'Esta publicacion no existe'}, status=status.HTTP_404_NOT_FOUND)  

def comentario_detail(request, pk):
    try: 
        comentario = Comentario.objects.get(pk=pk) 
    except comentario.DoesNotExist:
        return JsonResponse({'message': 'Este comentario no existe'}, status=status.HTTP_404_NOT_FOUND)  

 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def usuario_list_published(request):
    # GET all published tutorials
    usuario = Usuario.objects.filter(published=True)
        
    if request.method == 'GET': 
        usuario_serializer = UserSerializer(usuario, many=True)
        return JsonResponse(usuario_serializer.data, safe=False)

def publicacion_list_published(request):
    publicacion = Publicacion.objects.filter(published=True)
        
    if request.method == 'GET': 
        publicacion_serializer = PublicacionSerializers(publicacion, many=True)
        return JsonResponse(publicacion_serializer.data, safe=False)

def comentario_list_published(request):
    comentario = Comentario.objects.filter(published=True)
        
    if request.method == 'GET': 
        comentario_serializer = ComentarioSerializers(comentario, many=True)
        return JsonResponse(comentario_serializer.data, safe=False)


 
 

 
    
        
