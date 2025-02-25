from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('nova_venda/', views.nova_venda, name='nova_venda'),
    path('consultar_vendas/', views.consultar_vendas, name='consultar_vendas'),
    path('detalhes_venda/<int:venda_id>/', views.detalhes_venda, name='detalhes_venda'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('consulta_produtos/', views.consulta_produtos, name='consulta_produtos'),
    path('detalhes_produtos/<int:produtos_id>/', views.detalhes_produtos, name='detalhes_produtos'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('carrega_template/', views.carrega_template, name='carrega_template'),
]