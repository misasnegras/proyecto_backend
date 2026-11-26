from django import forms
from .models import Categoria, PerfilUsuario, Noticia, HistorialAuditoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'es_publica', 'activa']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'campo-texto',
                'placeholder': 'Ej: Política, Economía, Tecnología',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'campo-area',
                'rows': 3,
                'placeholder': 'Descripción breve de la sección editorial...',
            }),
            'es_publica': forms.CheckboxInput(attrs={
                'class': 'campo-check',
            }),
            'activa': forms.CheckboxInput(attrs={
                'class': 'campo-check',
            }),
        }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['usuario', 'rol', 'rut', 'telefono', 'activo']
        widgets = {
            'usuario': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'rol': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'rut': forms.TextInput(attrs={
                'class': 'campo-texto',
                'placeholder': 'Ej: 12.345.678-9',
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'campo-texto',
                'placeholder': 'Ej: +56 9 8765 4321',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'campo-check',
            }),
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'estado', 'visibilidad', 'vistas', 'autor', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'campo-texto',
                'placeholder': 'Titular de la noticia',
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'campo-area',
                'rows': 6,
                'placeholder': 'Cuerpo completo de la publicación periodística...',
            }),
            'estado': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'visibilidad': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'vistas': forms.NumberInput(attrs={
                'class': 'campo-numero',
                'min': 0,
            }),
            'autor': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'categoria': forms.Select(attrs={
                'class': 'campo-select',
            }),
        }


class HistorialAuditoriaForm(forms.ModelForm):
    class Meta:
        model = HistorialAuditoria
        fields = ['noticia', 'usuario_responsable', 'estado_anterior', 'estado_nuevo', 'observacion']
        widgets = {
            'noticia': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'usuario_responsable': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'estado_anterior': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'estado_nuevo': forms.Select(attrs={
                'class': 'campo-select',
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'campo-area',
                'rows': 3,
                'placeholder': 'Motivo o respaldo editorial del cambio de estado...',
            }),
        }