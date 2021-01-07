from Apps.usuario.models import Usuario,Publicacion,Comentario
from django.contrib.auth import login,logout
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','email','password']

class PublicacionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicacion 
        fields = ['titulo','foto','descripcion','titular']

class ComentarioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ['cuerpo','fecha','titular']




