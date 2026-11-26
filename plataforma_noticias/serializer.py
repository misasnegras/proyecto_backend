from rest_framework import serializers
from .models import Categoria, PerfilUsuario, Noticia, HistorialAuditoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = '__all__'


class HistorialAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialAuditoria
        fields = '__all__'