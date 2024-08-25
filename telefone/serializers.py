from rest_framework import serializers
from .models import Telefone

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone  # Modelo associado ao serializer
        fields = '__all__'  # Inclui todos os campos do modelo