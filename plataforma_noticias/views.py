from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, PerfilUsuario, Noticia, HistorialAuditoria
from .serializer import (
    CategoriaSerializer,
    PerfilUsuarioSerializer,
    NoticiaSerializer,
    HistorialAuditoriaSerializer,
)


def index(request):
    return render(request, 'index.html')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer


class HistorialAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = HistorialAuditoria.objects.all()
    serializer_class = HistorialAuditoriaSerializer