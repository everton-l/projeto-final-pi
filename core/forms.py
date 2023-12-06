from django import forms
from .models import Postagem, Flores

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'imagem' : forms.FileInput(attrs={'class':'form-control'}),
            'texto' : forms.TextInput(attrs={'class':'form-control'})
        }


class FlorForm(forms.ModelForm):
    class Meta:
        model = Flores
        fields = '__all__'
        widgets = {
            'nome_cientifico': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_popular': forms.TextInput(attrs={'class': 'form-control'}),
            'familia': forms.TextInput(attrs={'class': 'form-control'}),
            'bioma': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }


class FlorSearchForm(forms.Form):
    search_query = forms.CharField(label='Pesquisar', max_length=100, required=False)