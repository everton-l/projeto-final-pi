from django.shortcuts import render, get_object_or_404
from .models import Flores, Postagem
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import PostagemForm, FlorForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FlorListar(ListView):
    model = Flores
    template_name = 'flores.html'
    context_object_name = 'flor'
    paginate_by = 3

class FlorDetalhe(DetailView):
    model = Flores
    template_name = 'detalhe.html'
    context_object_name = 'flor'


class FlorCriar(CreateView):
    template_name = 'forms.html'
    form_class = Flores
    success_url = reverse_lazy('flor_listar')
    
    def get_success_url(self):
        return reverse_lazy('flor_listar')

class FlorEditar(UpdateView):
    model = Flores
    form_class = FlorForm
    template_name = 'form.html'
    pk_url_kwarg = 'pk' 
    
    def get_success_url(self):
        return reverse_lazy('flor_listar')

class FlorRemover(DeleteView):
    model = Flores
    success_url = reverse_lazy('flor_listar')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class PostagemCriar(CreateView):
    template_name = 'forms.html'
    form_class = PostagemForm
    success_url = reverse_lazy('postagem_listar')
    
    def get_success_url(self):
        return reverse_lazy('postagem_listar')