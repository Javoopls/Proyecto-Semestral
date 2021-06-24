from core.forms import NoticiaForm, RegistroForm
from django.shortcuts import render, redirect
from .models import Noticia

def index(request):
    return render(request,'core/index.html')

def contacto(request):
    return render(request,'core/contacto.html')

def login(request):
    return render(request,'core/login.html')

def noticia1(request):
    return render(request,'core/noticia1.html')

def noticia2(request):
    return render(request,'core/noticia2.html')

def noticia3(request):
    return render(request,'core/noticia3.html')

def password(request):
    return render(request,'core/password.html')

def index2(request):
    return render(request,'core/index2.html')

def api(request):
    return render(request, 'core/api.html')

def listaNoticia(request):
    listaNoticia= Noticia.objects.all()

    datos = {
        'lista': listaNoticia
    }

    return render(request, 'core/listaNoticia.html',datos)

def modNoticia(request, id):

    noticia = Noticia.objects.get(idNoticia=id)

    datos = {
        'formModNoticia': NoticiaForm(instance=noticia)
    }

    if request.method=='POST':
        formNoticia = NoticiaForm(data=request.POST, instance=noticia)

        if formNoticia.is_valid():
            formNoticia.save()

    return render(request,'core/modNoticia.html',datos)

def registrodjango(request):
    datos = {
        'formularioRegistro': RegistroForm()
    }

    if request.method=='POST':
        formRegistro = RegistroForm(request.POST)

        if formRegistro.is_valid:
            formRegistro.save()

    return render(request,'core/registrodjango.html',datos)

def noticiadjango(request):
    datos = {
        'formularioNoticia': NoticiaForm()
    }

    if request.method=='POST':
        formNoticia = NoticiaForm(request.POST, request.FILES)

        if formNoticia.is_valid():
            formNoticia.save()
    return render(request,'core/noticiadjango.html', datos)

def eliminarNoticia(request, id):

    noticia = Noticia.objects.get(idNoticia=id)

    noticia.delete()

    return redirect(to='listaNoticia')