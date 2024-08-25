from django.db import models
from django.contrib.auth.models import User

class Telefone(models.Model):
    numero = models.CharField(max_length=15, unique=True)  # Número do telefone
    nome = models.CharField(max_length=100)  # Nome associado ao telefone
    descricao = models.TextField()  # Descrição adicional

    def __str__(self):
        return self.numero  # Representação em string do objeto
    
class SeuModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.DateTimeField()

class TelefoneConsulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    data_consulta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.numero} - {self.data_consulta}'
    

class Consulta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_consultado = models.CharField(max_length=15)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.numero_consultado} em {self.data_hora}"
