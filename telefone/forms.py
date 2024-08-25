from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
        error_messages = {
            'password_mismatch': {
                'message': 'As senhas não correspondem.',
            },
        }

class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _('Usuário e/ou senha incorretos. Por favor, tente novamente.'),
        'inactive': _('Esta conta está inativa.'),
    }


    class Meta:
        fields = ['username', 'password']
        labels = {
            'username': 'Nome de usuário',
            'password': 'Senha',
        }
        help_texts = {
            'username': None,
            'password': None,
        }