from django.contrib import admin
from .models import Endereco

# Register your models here.
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'bairro', 'localidade', 'uf')
    search_fields =  ('cep', 'logradouro', 'bairro', 'localidade', 'uf')
    list_filter = ('localidade', 'uf')
    ordering = ['cep',]
