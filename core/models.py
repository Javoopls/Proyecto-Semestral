from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, TextField

# Create your models here.

# Modelo para Registro

class Registro(models.Model):
    nombreUser = models.CharField(max_length=50, verbose_name='Nombre del Usuario')
    correo = models.EmailField(max_length=40, primary_key=True, verbose_name='Correo')
    contrasenia = models.CharField(max_length=20, verbose_name='Contraseña')

    def __str__(self):
        return self.correo

# Modelo para Categoría Noticia

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoría')
    categoria = models.CharField(max_length=20, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.categoria

# Modelo para Creación de Noticia

class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True, verbose_name='Id Noticia')
    tituloNoticia = models.CharField(max_length=60, verbose_name='Título de la Noticia')
    autor = models.CharField(max_length=50, verbose_name='Autor Noticia')
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    imagen = models.ImageField(null=True, verbose_name='Imagen de Referencia')
    descNoticia = TextField(max_length=1000, verbose_name='Texto de Noticia')
    lugarNoticia = CharField(max_length=40, verbose_name='Lugar de los hechos')
    fechaNoticia = DateField(auto_now=False)

    def __str__(self):
        return self.tituloNoticia