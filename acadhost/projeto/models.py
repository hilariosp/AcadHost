from django.db import models

class Projeto(models.Model):
    autor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE, related_name='projetos_autoria')
    nome = models.CharField(max_length=200)
    introducao = models.TextField()
    resumo = models.TextField()
    referencial_teorico = models.TextField()
    desenvolvimento = models.TextField()
    resultados = models.TextField()
    conclusao = models.TextField()
    referencias = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(
        'Tag',
        through='ProjetoTag',
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.nome
    
class Tag(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class ProjetoTag(models.Model):
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('projeto', 'tag')

    def __str__(self):
        return f'{self.projeto.nome} → {self.tag.nome}'

