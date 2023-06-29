from django.db import models
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=50, null=False)   
