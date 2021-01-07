from django.urls import path
from .views import crearUsuario,crearPublicacion

urlpatterns = [
    path('crear_usuario/',crearUsuario,name='crear_usuario'),
    path('crear_publicacion/',crearPublicacion, name='crear_publicacion')

]