from django.urls import path
from .views import index, contacto, login, noticia1, noticia2, noticia3, password, index2, noticiadjango, registrodjango, modNoticia, api, listaNoticia, eliminarNoticia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index, name='index'),
    path('contacto/',contacto, name='contacto'),
    path('login/',login, name='login'),
    path('noticia1/',noticia1, name='noticia1'),
    path('noticia2/',noticia2, name='noticia2'),
    path('noticia3/',noticia3, name='noticia3'),
    path('password/',password, name='password'),
    path('index2/',index2, name='index2'),
    path('registrodjango/',registrodjango, name='registrodjango'),
    path('noticiadjango/crear-noticia/',noticiadjango, name='noticiadjango'),
    path('noticiadjango/mod-noticia/<id>',modNoticia, name='modNoticia'),
    path('noticiadjango/del-noticia/<id>',eliminarNoticia, name='eliminarNoticia'),
    path('apiClima/',api, name='apiClima'),
    path('noticiadjango/',listaNoticia,name='listaNoticia'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)