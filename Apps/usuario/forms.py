from django import forms
from .models import Usuario, Publicacion

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','edad','documento','email']

class PublicacionForms(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields =['foto','titulo','descripcion']
