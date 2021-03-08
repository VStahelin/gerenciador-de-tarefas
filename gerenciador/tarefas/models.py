from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    descricao = models.TextField()
    concluido = models.BooleanField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao