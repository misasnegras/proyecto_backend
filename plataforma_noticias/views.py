from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Categoria, PerfilUsuario, Noticia, HistorialAuditoria
from .forms import (
    CategoriaForm,
    PerfilUsuarioForm,
    NoticiaForm,
    HistorialAuditoriaForm,
)
from .serializer import (
    CategoriaSerializer,
    PerfilUsuarioSerializer,
    NoticiaSerializer,
    HistorialAuditoriaSerializer,
)


def index(request):
    return render(request, 'index.html')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/categoria_list.html'
    context_object_name = 'categorias'


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categorias/categoria_detail.html'
    context_object_name = 'categoria'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria_form.html'
    success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/categoria_confirm_delete.html'
    context_object_name = 'categoria'
    success_url = reverse_lazy('categoria_list')


class PerfilUsuarioListView(ListView):
    model = PerfilUsuario
    template_name = 'perfiles/perfil_list.html'
    context_object_name = 'perfiles'


class PerfilUsuarioDetailView(DetailView):
    model = PerfilUsuario
    template_name = 'perfiles/perfil_detail.html'
    context_object_name = 'perfil'


class PerfilUsuarioCreateView(CreateView):
    model = PerfilUsuario
    form_class = PerfilUsuarioForm
    template_name = 'perfiles/perfil_form.html'
    success_url = reverse_lazy('perfil_list')


class PerfilUsuarioUpdateView(UpdateView):
    model = PerfilUsuario
    form_class = PerfilUsuarioForm
    template_name = 'perfiles/perfil_form.html'
    success_url = reverse_lazy('perfil_list')


class PerfilUsuarioDeleteView(DeleteView):
    model = PerfilUsuario
    template_name = 'perfiles/perfil_confirm_delete.html'
    context_object_name = 'perfil'
    success_url = reverse_lazy('perfil_list')


class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticias/noticia_list.html'
    context_object_name = 'noticias'


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia_detail.html'
    context_object_name = 'noticia'


class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticia_form.html'
    success_url = reverse_lazy('noticia_list')


class NoticiaUpdateView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticia_form.html'
    success_url = reverse_lazy('noticia_list')


class NoticiaDeleteView(DeleteView):
    model = Noticia
    template_name = 'noticias/noticia_confirm_delete.html'
    context_object_name = 'noticia'
    success_url = reverse_lazy('noticia_list')


class HistorialAuditoriaListView(ListView):
    model = HistorialAuditoria
    template_name = 'auditoria/auditoria_list.html'
    context_object_name = 'auditorias'


class HistorialAuditoriaDetailView(DetailView):
    model = HistorialAuditoria
    template_name = 'auditoria/auditoria_detail.html'
    context_object_name = 'auditoria'


class HistorialAuditoriaCreateView(CreateView):
    model = HistorialAuditoria
    form_class = HistorialAuditoriaForm
    template_name = 'auditoria/auditoria_form.html'
    success_url = reverse_lazy('auditoria_list')


class HistorialAuditoriaUpdateView(UpdateView):
    model = HistorialAuditoria
    form_class = HistorialAuditoriaForm
    template_name = 'auditoria/auditoria_form.html'
    success_url = reverse_lazy('auditoria_list')


class HistorialAuditoriaDeleteView(DeleteView):
    model = HistorialAuditoria
    template_name = 'auditoria/auditoria_confirm_delete.html'
    context_object_name = 'auditoria'
    success_url = reverse_lazy('auditoria_list')


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