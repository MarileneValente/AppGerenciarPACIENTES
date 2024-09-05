from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
