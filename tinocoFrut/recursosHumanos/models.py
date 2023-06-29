from django.db import models

# Create your models here.
class RecursosHumanos(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    funcionario = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    cargaHoraria = models.DecimalField(max_digits=4,decimal_places=2)
    folhaPonto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    setor = models.CharField(max_length=80)
    
    