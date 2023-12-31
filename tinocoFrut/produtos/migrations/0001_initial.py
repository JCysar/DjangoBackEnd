# Generated by Django 4.2.1 on 2023-06-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidadeEstoque', models.IntegerField()),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=80, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
    ]
