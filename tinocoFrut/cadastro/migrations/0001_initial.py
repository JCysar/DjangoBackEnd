# Generated by Django 4.2.1 on 2023-06-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(default=None, max_length=80, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]