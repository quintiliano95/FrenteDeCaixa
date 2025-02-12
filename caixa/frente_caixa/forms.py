from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']


class AdicionarAoCarrinhoForm(forms.Form):
    quantidade = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))