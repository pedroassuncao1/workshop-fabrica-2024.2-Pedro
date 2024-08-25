from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Telefone
from .serializers import TelefoneSerializer
from django.http import HttpResponse
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import TelefoneConsulta
from django.contrib import messages




class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()  # Consulta todos os objetos de Telefone
    serializer_class = TelefoneSerializer  # Usa o serializer definido

    @action(detail=False, methods=['get'])
    def validar(self, request):
        numero = request.query_params.get('numero')
        if not numero:
            return Response({'error': 'Número não fornecido'}, status=400)

        # Faz a chamada para a API externa
        url = f'https://apilayer.net/api/validate?access_key=ba00d181148e6f3c2dad6b2c0cc8490c&number={numero}&country_code=BR&format=1'
        response = requests.get(url)
        data = response.json()

        if data.get('valid'):
            return Response(data)
        else:
            return Response({'error': 'Número inválido'}, status=400)
        
def informar_telefone(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero:
            url = f'https://apilayer.net/api/validate?access_key=ba00d181148e6f3c2dad6b2c0cc8490c&number={numero}&country_code=BR&format=1'
            response = requests.get(url)
            data = response.json()
            if data.get('valid'):
                # Registrar a consulta
                if request.user.is_authenticated:
                    TelefoneConsulta.objects.create(
                        usuario=request.user,
                        numero=numero,
                        data_consulta=timezone.now()
                    )
                return render(request, 'telefone/dados_telefone.html', {'data': data})
            else:
                return HttpResponse('Número inválido', status=400)
    return render(request, 'telefone/informar_telefone.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('informar_telefone')  # Redireciona após o registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'protected.html')

def consultar_telefone(request):
    telefones = Telefone.objects.all()
    return render(request, 'dados_telefone.html', {'telefones': telefones})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = '/informar_telefone/'  # URL para onde redirecionar após o login
    
    def get_success_url(self):
        return reverse_lazy('informar_telefone')
    
    def form_invalid(self, form):
        # Mensagem de erro personalizada
        messages.error(self.request, 'Usuário e/ou senha incorretos. Por favor, tente novamente.')
        return self.render_to_response(self.get_context_data(form=form))

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def home(request):
    return render(request, 'home.html')

@login_required
def informar_telefone(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        if numero:
            url = f'https://apilayer.net/api/validate?access_key=ba00d181148e6f3c2dad6b2c0cc8490c&number={numero}&country_code=BR&format=1'
            response = requests.get(url)
            data = response.json()
            if data.get('valid'):
                # Registrar a consulta
                if request.user.is_authenticated:
                    TelefoneConsulta.objects.create(
                        usuario=request.user,
                        numero=numero,
                        data_consulta=timezone.now()
                    )
                return render(request, 'telefone/dados_telefone.html', {'data': data})
            else:
                return HttpResponse('Número inválido', status=400)
    return render(request, 'telefone/informar_telefone.html')

@login_required
def historico_consultas(request):
    consultas = TelefoneConsulta.objects.filter(usuario=request.user).order_by('-data_consulta')
    return render(request, 'telefone/historico_consultas.html', {'consultas': consultas})
