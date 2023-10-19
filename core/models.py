from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='image')
    descricao = models.CharField(max_length=255, blank=True)

