from django.shortcuts import render, get_object_or_404, redirect
from .models import Flores, Postagem, Comentario
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import PostagemForm, FlorForm, FlorSearchForm, ComentarioForm
from django.db.models import Q
from usuarios.permissions import GerentePermission

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
                queryset = queryset.filter(
                    Q(nome_popular__icontains=search_query) | Q(nome_cientifico__icontains=search_query)
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = FlorSearchForm(self.request.GET)
        return context

class FlorDetalhe(DetailView):
    model = Flores
    template_name = 'detalhe.html'
    context_object_name = 'flor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(flor=self.object)
        context['comentario_form'] = ComentarioForm()
        return context

class FlorCriar(GerentePermission,CreateView):
    template_name = 'form-flor.html'
    form_class = FlorForm
    success_url = reverse_lazy('admin')
    
    def get_success_url(self):
        return reverse_lazy('admin')

class FlorEditar(GerentePermission,UpdateView):
    model = Flores
    form_class = FlorForm
    template_name = 'form-flor.html'
    pk_url_kwarg = 'pk' 
    
    def get_success_url(self):
        return reverse_lazy('admin')

class FlorRemover(GerentePermission,DeleteView):
    model = Flores
    success_url = reverse_lazy('admin')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class PostagemListar(ListView):
    model = Postagem
    template_name = 'flora.html'
    context_object_name = 'flora'

class PostagemCriar(GerentePermission,CreateView):
    template_name = 'form-postagem.html'
    form_class = PostagemForm
    success_url = reverse_lazy('admin')
    

class PostagemEditar(GerentePermission,UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'form-postagem.html'
    pk_url_kwarg = 'pk' 
    
    def get_success_url(self):
        return reverse_lazy('admin')

class PostagemRemover(GerentePermission,DeleteView):
    model = Postagem
    success_url = reverse_lazy('admin')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class AdminList(GerentePermission, ListView):
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

def sobre(request):
    return render(request, 'sobre.html')

def adicionar_comentario(request, pk):
    flor = get_object_or_404(Flores, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.flor = flor
            comentario.usuario = request.user
            comentario.save()
            return redirect('flor-detalhe', pk=pk)  # Redireciona para a página de detalhe da flor
    else:
        form = ComentarioForm()
    
    comentarios = Comentario.objects.filter(flor=flor)
    return render(request, 'detalhe.html', {'flor': flor, 'comentarios': comentarios, 'comentario_form': form})

def remover_comentario(request, pk_flor, pk_comentario):
    flor = get_object_or_404(Flores, pk=pk_flor)
    comentario = get_object_or_404(Comentario, pk=pk_comentario, usuario=request.user)
    comentario.delete()
    return redirect('flor-detalhe', pk=pk_flor)
