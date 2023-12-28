"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('flor/', views.FlorListar.as_view(), name='listagem'),
    path('flor/editar/<int:pk>/', login_required(views.FlorEditar.as_view()), name='flor-editar'),
    path('flor/detalhe/<int:pk>/', views.FlorDetalhe.as_view(), name='flor-detalhe'),
    path('flor/adicionar_comentario/<int:pk>/', views.adicionar_comentario, name='adicionar_comentario'),
    path('flor/remover_comentario/<int:pk_flor>/<int:pk_comentario>/', login_required(views.remover_comentario), name='remover_comentario'),
    path('flor-remover/<int:pk>/', login_required(views.FlorRemover.as_view()), name='flor-remover'),
    path('form-flor/', login_required(views.FlorCriar.as_view()), name='flor-criar'),
    path('form-post/', login_required(views.PostagemCriar.as_view()), name='postagem-criar'),
    path('flora/', views.PostagemListar.as_view(), name="flora"),
    path('postagem/editar/<int:pk>/', login_required(views.PostagemEditar.as_view()), name='post-editar'),
    path('postagem/remover/<int:pk>/', login_required(views.PostagemRemover.as_view()), name='post-remover'),
    path('administração/', login_required(views.AdminList.as_view()), name='admin'),
    path('sobre/', views.sobre, name='sobre'),
    path('accounts/',include('usuarios.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
