# Generated by Django 4.0.3 on 2022-04-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_de_estoque', '0004_alter_produto_data_cadastro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]