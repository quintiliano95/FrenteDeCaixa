from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import *
from .forms import *


def homepage(request):
    return render(request, 'homepage.html')


def nova_venda(request):
    if request.method == "POST":
        # Captura os dados da venda
        produtos = request.POST.getlist("produtos[]")
        quantidades = request.POST.getlist("quantidades[]")

        if not produtos or not quantidades:
            return JsonResponse({"erro": "Nenhum produto foi adicionado."}, status=400)

        # Criar a venda
        venda = Venda.objects.create()

        # Adicionar os itens da venda
        total = 0
        for i in range(len(produtos)):
            produto = Produto.objects.get(id=produtos[i])
            quantidade = int(quantidades[i])
            subtotal = produto.preco * quantidade

            ItemVenda.objects.create(venda=venda, produto=produto, quantidade=quantidade, subtotal=subtotal)

            total += subtotal

        # Atualiza o total da venda
        venda.total = total
        venda.save()

        return JsonResponse({"mensagem": "Venda realizada com sucesso!", "venda_id": venda.id})

    produtos = Produto.objects.all()
    return render(request, "nova_venda.html", {"produtos": produtos})

def consultar_vendas(request):
    vendas = Venda.objects.all().order_by('id')
    return render(request, 'consultar_vendas.html', {"vendas": vendas})

def detalhes_venda(request, venda_id):
    try:
        venda = Venda.objects.get(id=venda_id)
        itens = ItemVenda.objects.filter(venda=venda)

        detalhes = [
            {
                "produto": item.produto.nome,
                "quantidade": item.quantidade,
                "subtotal": float(item.subtotal),
            }
            for item in itens
        ]

        return JsonResponse({"itens": detalhes})

    except Venda.DoesNotExist:
        return JsonResponse({"erro": "Venda não encontrada"}, status=404)


def carrinho(request):
    return render(request, 'carrinho.html')

def consulta_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'consulta_produtos.html', {"produtos": produtos})


def detalhes_produtos(request, produtos_id):
    try:
        produtos = Produto.objects.get(id=produtos_id)
        itens = ItemVenda.objects.filter(venda=produtos)

        detalhes = [
            {
                "produto": item.produto.nome,
                "quantidade": item.quantidade,
                "subtotal": float(item.subtotal),
            }
            for item in itens
        ]

        return JsonResponse({"itens": detalhes})

    except Venda.DoesNotExist:
        return JsonResponse({"erro": "Venda não encontrada"}, status=404)


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        if 'excluir' in request.POST:  # Verifica se o botão "Excluir" foi pressionado
            produto.delete()  # Exclui o produto
            return redirect('consulta_produtos')  # Redireciona de volta para a lista de produtos
        else:
            form = EditarProdutoForm(request.POST, instance=produto)
            if form.is_valid():
                form.save()
                return redirect('consulta_produtos')  # Redireciona de volta para a lista de produtos
    else:
        form = EditarProdutoForm(instance=produto)

    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})


def adicionar_produto(request):
    if request.method == 'POST':
        form = EditarProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_produtos')  # Redireciona para a lista de produtos
    else:
        form = EditarProdutoForm()

    return render(request, 'adicionar_produto.html', {'form': form})


def cadastrar_cliente(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        endereco = request.POST.get("endereco")

        if nome and cpf:  # Validação simples
            Cliente.objects.create(
                nome=nome,
                cpf=cpf,
                email=email,
                telefone=telefone,
                endereco=endereco
            )

        return JsonResponse({"success": True, "message": "Cliente cadastrado com sucesso!"})
    return render(request, "cadastrar_cliente.html")