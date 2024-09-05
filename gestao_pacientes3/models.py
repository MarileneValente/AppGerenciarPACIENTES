from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome
