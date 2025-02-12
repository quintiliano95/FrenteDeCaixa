from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Venda, Carrinho
from .forms import ProdutoForm, AdicionarAoCarrinhoForm


def homepage(request):
    return render(request, 'homepage.html')


def nova_venda(request):
    return render(request, 'nova_venda.html')

def consultar_vendas(request):
    return render(request, 'consultar_vendas.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def consulta_produtos(request):
    return render(request, 'consulta_produtos.html')