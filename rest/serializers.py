from django.db.models.base import Model
from rest_framework import fields, serializers
from core.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['idNoticia','tituloNoticia','autor','categoria','imagen','descNoticia','lugarNoticia','fechaNoticia']