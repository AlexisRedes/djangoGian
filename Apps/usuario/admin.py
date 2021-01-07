from django.contrib import admin
from Apps.usuario.models import Usuario, Publicacion, Comentario
from django.contrib.auth.admin import UserAdmin

class PersonalizoUserAdmin(UserAdmin):
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('nombreDeUsuario', 'password1', 'password2')
            }),
    )
    list_display = ('nombreDeUsuario','is_active','is_staff')
    search_fields =('nombreDeUsuario',)
    ordering =('nombreDeUsuario',)
admin.site.register(Usuario,PersonalizoUserAdmin)
admin.site.register(Publicacion)
admin.site.register(Comentario)
