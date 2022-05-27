# Generated by Django 4.0.3 on 2022-04-20 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sistema_de_estoque', '0002_remove_produto_categoria_delete_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.FloatField()),
                ('descricao', models.CharField(max_length=200)),
                ('data_cadastro', models.DateField()),
                ('data_update', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_de_estoque.categoria')),
            ],
            options={
                'verbose_name_plural': 'Produto',
            },
        ),
    ]