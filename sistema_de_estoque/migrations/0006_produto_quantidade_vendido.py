# Generated by Django 4.0.3 on 2022-04-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_de_estoque', '0005_produto_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade_vendido',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
