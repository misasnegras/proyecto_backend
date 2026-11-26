from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    es_publica = models.BooleanField(default=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    ROLES = [
        ('AUTOR', 'Autor / Periodista'),
        ('EDITOR', 'Editor'),
        ('LECTOR', 'Lector'),
        ('ADMIN', 'Administrador'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=15, choices=ROLES, default='LECTOR')
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} ({self.rol})"


class Noticia(models.Model):
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('EN_REVISION', 'En Revisión'),
        ('PUBLICADA', 'Publicada'),
        ('ARCHIVADA', 'Archivada'),
    ]

    VISIBILIDADES = [
        ('PUBLICA', 'Pública'),
        ('PRIVADA', 'Privada'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='BORRADOR')
    visibilidad = models.CharField(max_length=15, choices=VISIBILIDADES, default='PUBLICA')
    vistas = models.PositiveIntegerField(default=0)
    autor = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT, related_name='noticias')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='noticias')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class HistorialAuditoria(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='historial')
    usuario_responsable = models.ForeignKey(PerfilUsuario, on_delete=models.PROTECT)
    estado_anterior = models.CharField(max_length=20, choices=Noticia.ESTADOS)
    estado_nuevo = models.CharField(max_length=20, choices=Noticia.ESTADOS)
    observacion = models.TextField(blank=True)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.noticia.titulo}: {self.estado_anterior} -> {self.estado_nuevo}"