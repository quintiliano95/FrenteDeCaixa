from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('nova_venda/', views.nova_venda, name='nova_venda'),
    path('consultar_vendas/', views.consultar_vendas, name='consultar_vendas'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('consulta_produtos/', views.consulta_produtos, name='consulta_produtos'),
]