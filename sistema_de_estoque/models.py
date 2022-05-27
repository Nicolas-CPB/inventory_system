from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    class Meta(object):
        verbose_name_plural = 'Categoria'
        
    categoria = models.CharField(max_length=20)
    def __str__(self):
        return self.categoria
    
class Produto(models.Model):
    class Meta(object):
        verbose_name_plural = 'Produto'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    quantidade_vendido = models.IntegerField(default="0")
    lucro = models.FloatField(default="0")
    data_cadastro = models.CharField(max_length=10)
    data_update = models.CharField(max_length=10)
    def __str__(self):
        return self.nome