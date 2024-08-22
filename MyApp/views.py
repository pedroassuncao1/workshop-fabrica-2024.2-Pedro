from django.shortcuts import render
from .models import Endereco
from django.shortcuts import get_object_or_404, render, redirect
import requests
from .forms import enderecoForm

"""criar uma função para consumir a API"""
def buscar_enderecoView(request):
    endereco = None
    form = enderecoForm(request.GET or None)

    if form.is_valid():
        cep = form.cleaned_data['cep']
        response = request.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200: 
            dados_endereco = response.json()
            endereco = Endereco.objects.create(
                cep = cep,
                logradouro = dados_endereco.get('logradouro'),
                bairro = dados_endereco.get('bairro'),
                localidade = dados_endereco.get('localidade'),
                uf = dados_endereco.get('uf'),
            )
    return render(request, 'consultaCEP.html', {'form':form, 'endereco': endereco})

def listar_endereco(request):
    enderecos = Endereco.objects.all()
    return render(request, 'listar_endereco.html', {'enderecos': enderecos})

# Create your views here.

