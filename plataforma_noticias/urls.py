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

    # CRUD Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/nueva/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    # CRUD Perfiles de Usuario
    path('perfiles/', views.PerfilUsuarioListView.as_view(), name='perfil_list'),
    path('perfiles/<int:pk>/', views.PerfilUsuarioDetailView.as_view(), name='perfil_detail'),
    path('perfiles/nuevo/', views.PerfilUsuarioCreateView.as_view(), name='perfil_create'),
    path('perfiles/<int:pk>/editar/', views.PerfilUsuarioUpdateView.as_view(), name='perfil_update'),
    path('perfiles/<int:pk>/eliminar/', views.PerfilUsuarioDeleteView.as_view(), name='perfil_delete'),

    # CRUD Noticias
    path('noticias/', views.NoticiaListView.as_view(), name='noticia_list'),
    path('noticias/<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia_detail'),
    path('noticias/nueva/', views.NoticiaCreateView.as_view(), name='noticia_create'),
    path('noticias/<int:pk>/editar/', views.NoticiaUpdateView.as_view(), name='noticia_update'),
    path('noticias/<int:pk>/eliminar/', views.NoticiaDeleteView.as_view(), name='noticia_delete'),

    # CRUD Historial de Auditoría
    path('auditoria/', views.HistorialAuditoriaListView.as_view(), name='auditoria_list'),
    path('auditoria/<int:pk>/', views.HistorialAuditoriaDetailView.as_view(), name='auditoria_detail'),
    path('auditoria/nuevo/', views.HistorialAuditoriaCreateView.as_view(), name='auditoria_create'),
    path('auditoria/<int:pk>/editar/', views.HistorialAuditoriaUpdateView.as_view(), name='auditoria_update'),
    path('auditoria/<int:pk>/eliminar/', views.HistorialAuditoriaDeleteView.as_view(), name='auditoria_delete'),

    path('api/', include(router.urls)),
]