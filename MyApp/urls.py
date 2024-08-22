from django.urls import path, include
from .views import buscar_enderecoView, listar_endereco



urlpatterns = [
    path('buscar-cep/', buscar_enderecoView, name='buscar_cep'),
    path('listar_endereco/', listar_endereco, name='listar_cep')
]