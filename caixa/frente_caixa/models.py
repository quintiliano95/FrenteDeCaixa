from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} - {self.total()}"