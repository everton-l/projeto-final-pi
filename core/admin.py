from django.contrib import admin
from .models import Postagem
# Register your models here.

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem', 'descricao')

admin.site.register(Postagem, PostagemAdmin)