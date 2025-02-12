from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Venda, Carrinho
from .forms import ProdutoForm, AdicionarAoCarrinhoForm


def homepage(request):
    return render(request, 'homepage.html')


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


def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = AdicionarAoCarrinhoForm(request.POST)
        if form.is_valid():
            quantidade = form.cleaned_data['quantidade']
            # Verifica se o produto já está no carrinho
            item_carrinho, created = Carrinho.objects.get_or_create(produto=produto)
            if not created:
                item_carrinho.quantidade += quantidade
            else:
                item_carrinho.quantidade = quantidade
            item_carrinho.save()
            return redirect('ver_carrinho')
    else:
        form = AdicionarAoCarrinhoForm()
    return render(request, 'adicionar_ao_carrinho.html', {'form': form, 'produto': produto})

def ver_carrinho(request):
    itens_carrinho = Carrinho.objects.all()
    total_carrinho = sum(item.total_item() for item in itens_carrinho)
    return render(request, 'ver_carrinho.html', {'itens_carrinho': itens_carrinho, 'total_carrinho': total_carrinho})