# Generated by Django 4.0.3 on 2022-04-20 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_de_estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
