# Generated by Django 4.2.1 on 2023-06-28 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_alter_financeiro_comprar_alter_financeiro_vender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeiro',
            name='fiscal',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
