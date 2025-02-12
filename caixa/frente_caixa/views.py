from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Produto, Venda, ItemVenda


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