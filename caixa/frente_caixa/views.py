from django.shortcuts import render, redirect
from .models import Produto, Venda
from .forms import ProdutoForm


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})


def registrar_venda(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        quantidade = int(request.POST['quantidade'])
        Venda.objects.create(produto=produto, quantidade=quantidade)
        return redirect('lista_produtos')
    return render(request, 'registrar_venda.html', {'produto': produto})


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Redireciona para a lista de produtos após salvar
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})