from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    TIPOS = (
        ('aluno', 'Aluno'),
        ('orientador', 'Orientador'),
        ('avaliador', 'Avaliador'),
    )

    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    matricula = models.CharField(max_length=20, unique=True, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPOS, blank=True, null=True)
    add_em = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - ({self.tipo})'

class Equipe(models.Model):
    FUNCOES = (
        ('autor', 'Autor'),
        ('orientador', 'Orientador'),
        ('colaborador', 'Colaborador'),
    )

    membro = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    projeto = models.ForeignKey('projeto.Projeto', on_delete=models.CASCADE)
    funcao = models.CharField(max_length=20, choices=FUNCOES)
    data_entrada = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('membro', 'projeto')
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Membros da Equipe'

    def __str__(self):
        return f'{self.usuario.nome} - {self.projeto.titulo} ({self.funcao})'