from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class PersonalizadoBaseUserManage(BaseUserManager):
    def create_user(self,nombreDeUsuario,password):
        user = self.model(nombreDeUsuario=nombreDeUsuario)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,nombreDeUsuario,password):
        user = self.create_user(nombreDeUsuario,password)
        user.is_staff = False
        user.is_superuser =True
        user.save(using=self._db)
        return user

    
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nombreDeUsuario= models.CharField(max_length=20, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=10, blank=False, null=False)
    apellido = models.CharField(max_length=20, blank=False, null=False)
    edad = models.CharField(max_length=2, blank=False, null=False)
    documento = models.CharField(max_length=8, blank=False, null=False)
    email = models.EmailField(null=True,blank=True)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    USERNAME_FIELD = 'nombreDeUsuario'

    def get_full_name(self):
        return self.nombreDeUsuario
    
    def get_short_name(self):
        return self.nombre
    
    def __str__(self):
        return self.nombreDeUsuario
        
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']

    
    objects = PersonalizadoBaseUserManage()


class Publicacion(models.Model):
    id= models.AutoField(primary_key=True)
    foto = models.ImageField(null=True)
    titulo = models.CharField(max_length=30,blank=False, null=False)
    descripcion= models.TextField(max_length=300,null=True,blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    titular = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True)

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    cuerpo = models.TextField(max_length=300,null=True,blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    titular = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True)








