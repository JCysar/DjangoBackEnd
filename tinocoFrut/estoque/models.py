from django.db import models

# Create your models here.
class Estoque(models.Model):
    setor = models.CharField(max_length=100, null=False)
    corredor = models.IntegerField(null=False)
    prateleira = models.IntegerField(null=False)
    produto = models.CharField(max_length=80, null=False, unique=True)
    