from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Produto, Categoria
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

@login_required(redirect_field_name='login')
def index(request):
    Produtos = Produto.objects.all().order_by('-id').filter(user=request.user)
    paginator = Paginator(Produtos, 4)
    page = request.GET.get('p')
    Produtos = paginator.get_page(page)
    return render(request, 'paginas/index.html', {'Produtos':Produtos})

@login_required(redirect_field_name='login')
def change_password(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        check = auth.authenticate(request, username=user, password=password)
        user = User.objects.get(id=request.user.id)
        if check is not None:
            if password == "" or new_password == "" or confirm_new_password == "":
                messages.info(request, 'Preencha todos os campos!')
                return render(request, 'paginas/change_password.html')

            elif new_password != confirm_new_password:
                messages.info(request, 'As senhas não são iguais!')
                return render(request, 'paginas/change_password.html')
            else:
                user.set_password(new_password)
                user.save()
                return redirect('home')
        else:
            messages.info(request, 'Senha antiga incorreta')
            return render(request, 'paginas/change_password.html')
    else:  
        return render(request, 'paginas/change_password.html')

@login_required(redirect_field_name='login')
def adicionar_produto(request):
    Categorias = Categoria.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        data_cadastro = datetime.today().strftime('%d-%m-%Y')
        data_update = datetime.today().strftime('%d-%m-%Y')
        quantidade = request.POST.get('quantidade')
        
        add = Produto.objects.create(
            user=request.user, 
            nome=nome, 
            categoria_id=categoria, 
            valor=valor, 
            descricao=descricao, 
            data_cadastro=data_cadastro, 
            quantidade=quantidade, 
            data_update=data_update
        )
        add.save()
        return redirect('home')
    else:
        return render(request, 'paginas/adicionar_produto.html', {'Categorias':Categorias})
















@login_required(redirect_field_name='login')
def compra(request, id):
    compra = get_object_or_404(Produto, id=id)
    if compra.quantidade == 0:
        messages.info(request, message="Produto esgotado")
    else:
        compra.quantidade -= 1
        compra.data_update = datetime.today().strftime('%d-%m-%Y')
        compra.quantidade_vendido += 1
        compra.lucro = compra.quantidade_vendido * compra.valor
        compra.lucro = round(compra.lucro, 3)
        compra.save()
    return redirect('home')

@login_required(redirect_field_name='login')
def repor(request, id):
    repor = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        numero = request.POST.get("numero")
        repor.quantidade += int(numero)
        repor.data_update = datetime.today().strftime('%Y-%m-%d')
        repor.save()
        return redirect('home')
    else:
        return render(request, 'paginas/repor_produto.html', {'produto': repor})