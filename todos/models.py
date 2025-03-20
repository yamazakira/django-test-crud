from django.db import models

# Create your models here.

# Camada relacionada a base de dados; classes que representam as entidades que estamos trabalhando.


class Todo(models.Model):
    # Null => Campo vazio; Blank => Campo preenchido com espaços
    title = models.CharField(max_length=400, null=False, blank=False)
    # auto_now_add = true : Adiciona a informação da hora atual
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)
