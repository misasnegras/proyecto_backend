from django.contrib import admin
from .models import Categoria, PerfilUsuario, Noticia, HistorialAuditoria

admin.site.register(Categoria)
admin.site.register(PerfilUsuario)
admin.site.register(Noticia)
admin.site.register(HistorialAuditoria)