from django.db import models

# Create your models here.
class Financeiro(models.Model):
    comprar = models.CharField(max_length=50)
    vender = models.CharField(max_length=50)
    fiscal = models.CharField(max_length=100, unique=True)
    relatorioCompra = models.TextField(max_length=100)
    relatorioVenda = models.TextField(max_length=100)