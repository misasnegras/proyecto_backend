from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'perfiles', views.PerfilUsuarioViewSet)
router.register(r'noticias', views.NoticiaViewSet)
router.register(r'auditoria', views.HistorialAuditoriaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]