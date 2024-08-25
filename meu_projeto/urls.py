from django.contrib import admin
from django.urls import path
from telefone import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('admin/', admin.site.urls),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('protected/', views.protected_view, name='protected'),
    path('consultar_telefone/', views.consultar_telefone, name='consultar_telefone'),
    path('informar_telefone/', views.informar_telefone, name='informar_telefone'),
    path('home/', views.home, name='home'),  # Corrigido para 'home' em vez de ''
]