from django.contrib import admin
from .models import Postagem, Bioma, Flores, Comentario
# Register your models here.

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'image', 'texto')

class BiomaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class FloresAdmin(admin.ModelAdmin):
    list_display = ('nome_cientifico', 'nome_popular', 'familia', 'bioma', 'imagem', 'descricao', 'comentarios_count')

    def comentarios_count(self, obj):
        return obj.comentarios.count()

admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Bioma, BiomaAdmin)
admin.site.register(Flores, FloresAdmin)
admin.site.register(Comentario)