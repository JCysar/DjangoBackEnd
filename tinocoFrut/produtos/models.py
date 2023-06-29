from django.db import models

# Create your models here.
class Produto(models.Model):
    quantidadeEstoque = models.IntegerField(null=False)
    descricao = models.TextField()
    nome = models.CharField(max_length=80, null=False, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=100, null=False)