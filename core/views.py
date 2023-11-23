from django.shortcuts import render, get_object_or_404
from .models import Postagem
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FlorDetalhe(DetailView):
    model = Postagem
    template_name = 'detalhe.html'
    context_object_name = 'flor'

class FlorListar(ListView):
    model = Postagem
    template_name = 'flores.html'
    context_object_name = 'flor'
    paginate_by = 5

    def flor_detalhe(request, id):
        return FlorDetalhe.as_view()(request, id=id)


class FlorCriar(CreateView):
    template_name = 'forms.html'
    form_class = Postagem
    success_url = reverse_lazy('flor_listar')
    
    def get_success_url(self):
        return reverse_lazy('flor_listar')