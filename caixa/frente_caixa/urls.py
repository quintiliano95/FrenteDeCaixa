from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('registrar_venda/<int:produto_id>/', views.registrar_venda, name='registrar_venda'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),  # Nova URL
]