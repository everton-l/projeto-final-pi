from django.shortcuts import render, get_object_or_404
from .models import Flores, Postagem
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import PostagemForm, FlorForm, FlorSearchForm

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
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FlorSearchForm(self.request.GET)

        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            if search_query:
                queryset = queryset.filter(nome_popular__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = FlorSearchForm(self.request.GET)
        return context

class FlorDetalhe(DetailView):
    model = Flores
    template_name = 'detalhe.html'
    context_object_name = 'flor'

class FlorCriar(CreateView):
    template_name = 'form-flor.html'
    form_class = FlorForm
    success_url = reverse_lazy('admin')
    
    def get_success_url(self):
        return reverse_lazy('admin')

class FlorEditar(UpdateView):
    model = Flores
    form_class = FlorForm
    template_name = 'form-flor.html'
    pk_url_kwarg = 'pk' 
    
    def get_success_url(self):
        return reverse_lazy('admin')

class FlorRemover(DeleteView):
    model = Flores
    success_url = reverse_lazy('admin')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class PostagemListar(ListView):
    model = Postagem
    template_name = 'flora.html'
    context_object_name = 'flora'

class PostagemCriar(CreateView):
    template_name = 'form-postagem.html'
    form_class = PostagemForm
    success_url = reverse_lazy('admin')
    
    def get_success_url(self):
        return reverse_lazy('admin')

class PostagemEditar(UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'form-postagem.html'
    pk_url_kwarg = 'pk' 
    
    def get_success_url(self):
        return reverse_lazy('admin')

class PostagemRemover(DeleteView):
    model = Postagem
    success_url = reverse_lazy('admin')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class AdminList(ListView):
    template_name = 'list-forms.html'
    context_object_name = 'itens'

    def get_queryset(self):
        flores = Flores.objects.all()
        postagens = Postagem.objects.all()
        return list(flores) + list(postagens)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flor'] = Flores.objects.all()
        context['post'] = Postagem.objects.all()
        return context

def negado(request):
    return render(request, 'negado.html')

def sobre(request):
    return render(request, 'sobre.html')
