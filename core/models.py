from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=10)
    imagem = models.ImageField(upload_to='image', blank=True)
    texto = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.titulo

class Bioma(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome

class Flores(models.Model):
    nome_cientifico = models.CharField(max_length=200)
    nome_popular = models.CharField(max_length=200)
    familia = models.CharField(max_length=200)
    bioma = models.ForeignKey(Bioma, on_delete=models.CASCADE, blank=True, null=True)
    imagem = models.ImageField(upload_to='image')
    descricao = models.CharField(max_length=255, blank=True)

   