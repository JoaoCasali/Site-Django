from django.db import models


class Alunos(models.Model):
    nome_aluno = models.CharField(max_length=150)

    descricao_proficional = models.TextField()

    descricao_pessoal = models.TextField()

    habilidades = models.CharField(max_length=150)

    comportamento = models.CharField(max_length=150)

    workspace = models.CharField(max_length=150)

    categoria = models.CharField(max_length=150)

    date_aluno = models.DateTimeField(auto_now=True, auto_now_add=False)
