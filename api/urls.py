from django.urls import path, include
from rest_framework import routers
from api import views


router_usuario = routers.DefaultRouter()
router_usuario.register(r'usuarios', views.UserViewSet)
router_publicacion = routers.DefaultRouter()
router_publicacion.register(r'publicacion', views.PublicacionViewSet)
router_comentario = routers.DefaultRouter()
router_comentario.register(r'comentario', views.ComentarioViewSet)

urlpatterns = [ 

    path('router_usuario/', include(router_usuario.urls)),
    path('router_publicacion/', include(router_publicacion.urls)),
    path('router_comentario/', include(router_comentario.urls)),


]


#path('api_usuario/',views.usuario_list),
#path('api_usuario_details/',views.usuario_detail),
#path('api_usuarios_published/',views.usuario_list_published),

#path('api_publicaciones/',views.publicacion_list),
#path('api_publicaciones_details/',views.publicacion_detail),
#path('api_publicaciones_published/',views.publicacion_list_published)