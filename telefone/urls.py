from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelefoneViewSet
from .views import informar_telefone
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.shortcuts import redirect

router = DefaultRouter()
router.register(r'telefones', TelefoneViewSet)  # Registra o viewset com a URL /telefones/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('consultar_telefone')),  # Redireciona para a URL 'consultar_telefone'
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('consultar_telefone/', views.consultar_telefone, name='consultar_telefone'),
    path('informar_telefone/', views.informar_telefone, name='informar_telefone'),
    
]