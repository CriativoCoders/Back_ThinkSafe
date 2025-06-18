from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    NI = models.CharField(max_length=255, blank=True, null=True)
    is_instructor = models.BooleanField(default=False)

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    edv = models.CharField(max_length=8)
    data_aniversario = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    professor_responsavel = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_instructor': True}, null=True, related_name='cursos_responsaveis')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)
    professor_responsavel = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_instructor': True}, null=True)
    def __str__(self):
        return self.nome