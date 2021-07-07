from django.urls import path
from rest.views import detalle_noticia, procesar_noticias

urlpatterns = [
    path('noticias', procesar_noticias, name="procesar_noticias"),
    path('noticias/<id>', detalle_noticia, name="detalle_noticia")
]