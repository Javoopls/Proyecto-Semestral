from django.shortcuts import render
from .serializers import NoticiaSerializer
from rest_framework.serializers import Serializer
from django.shortcuts import render
from core.models import Noticia
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

def procesar_noticias(request):
    if request.method == 'GET' : 
        noticias = Noticia.objects.all()
        serializer = NoticiaSerializer(noticias,many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_noticia(request, id):
    try:
        noticia = Noticia.objects.get(idNoticia=id)
    except Noticia.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoticiaSerializer(noticia)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(noticia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    if request.method == 'DELETE' :
        noticia.delete()
        return Response(status.HTTP_204_NO_CONTENT)