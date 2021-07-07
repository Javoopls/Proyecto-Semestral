from django.urls import path
from .views import detalle_noticia, procesar_noticias
from .viewslogin import login

urlpatterns = [
    path('noticias', procesar_noticias, name="procesar_noticias"),
    path('noticias/<id>', detalle_noticia, name="detalle_noticia"),
    path('login',login, name='login')
]