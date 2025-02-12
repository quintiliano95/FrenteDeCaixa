from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('registrar_venda/<int:produto_id>/', views.registrar_venda, name='registrar_venda'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('ver_carrinho/', views.ver_carrinho, name='ver_carrinho'),
]