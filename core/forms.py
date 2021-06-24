from .models import Registro, Noticia
from django.forms import ModelForm
from django import forms

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['nombreUser','correo','contrasenia']

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['idNoticia','tituloNoticia','autor','categoria','imagen','descNoticia','lugarNoticia','fechaNoticia']