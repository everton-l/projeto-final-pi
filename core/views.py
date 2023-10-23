from django.shortcuts import render, get_object_or_404
from .models import Postagem

# Create your views here.

def index(request):
    return render(request, 'index.html', context={})

def caatinga(request):
    return render(request, 'caatinga.html', context={})

def flora(request):
    return render(request, 'flora.html', context={})

def estado(request):
    return render(request, 'estado.html', context={})

def listagem(request):
    postagem = Postagem.objects.all()
    context = {'postagens' : postagem}
    return render(request, 'flores.html', context)

def detalhe(request, id):
    postagem = get_object_or_404(Postagem, id=id)
    return render(request, 'detalhe.html', context={'postagem':postagem})

def form(request):
    return render(request, 'forms.html', context={})