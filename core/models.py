from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image-post', blank=True)
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
    bioma = models.ForeignKey(Bioma, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='image')
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome_popular


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    flor = models.ForeignKey(Flores, related_name='comentarios', on_delete=models.CASCADE, null=True)