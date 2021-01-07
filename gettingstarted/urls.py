from django.urls import path, include

from django.contrib import admin
admin.autodiscover()
from Apps.usuario.views import Home, crearUsuario
from rest_framework.authtoken import views


urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('usuario/', include(('Apps.usuario.urls','usuario'))),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_generate_token/',views.obtain_auth_token),
]
