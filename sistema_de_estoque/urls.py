from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('change_password/', views.change_password, name='change_password'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('compra/<int:id>', views.compra, name='compra'),
    path('repor_produto/<int:id>', views.repor, name='repor'),
]