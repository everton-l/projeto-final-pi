from django.contrib import admin
from .models import Postagem, Bioma, Flores
# Register your models here.

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem', 'texto')

class BiomaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class FloresAdmin(admin.ModelAdmin):
    list_display = ('nome_cientifico', 'nome_popular', 'familia', 'bioma', 'imagem', 'descricao')

admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Bioma, BiomaAdmin)
admin.site.register(Flores, FloresAdmin)