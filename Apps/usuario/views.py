from django.shortcuts import render, redirect, HttpResponseRedirect
from Apps.usuario.forms import UsuarioForms, PublicacionForms

def Home(request):
    return render(request,'index.html')

def crearUsuario(request):
    if request.method=='POST':
        usuario_form=UsuarioForms(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('index')
    else:
        usuario_form= UsuarioForms()
    return render(request,'usuario/crear_usuario.html',{'usuario_form':usuario_form})

def crearPublicacion(request):
    if request.method=='POST':
        publicacion_form=PublicacionForms(request.POST)
        if publicacion_form.is_valid():
            publicacion_form.save()
            return redirect('index')
    else:
        publicacion_form = PublicacionForms()
    return render(request, 'usuario/crear_publicacion.html',{'publicacion_form':publicacion_form})

    

