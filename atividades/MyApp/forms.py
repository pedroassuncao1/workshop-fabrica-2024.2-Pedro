from django import forms 
from .models import Endereco 

class enderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco 
        fields = ['cep']
        labels = {
            'cep': 'CEP',
        }
        widgets = { 
            'cep': forms.TextInput(attrs={'placeholder': 'Digite um CEP','max_length': '8'}),
        }