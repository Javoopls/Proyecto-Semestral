from django.contrib import admin
from .models import Registro, Categoria, Noticia

# Permite administrar el modelo completo

admin.site.register(Registro)
admin.site.register(Categoria)
admin.site.register(Noticia)