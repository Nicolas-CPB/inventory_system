from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        check = auth.authenticate(request, username=user, password=password)
        if check is not None:
            login(request, check)
            return redirect('home')
        else:
            if user == "":
                messages.info(request, 'Usuário inválido, por favor preencha todos os campos')
                return render(request, 'paginas/login.html')
            elif password == "":
                messages.info(request, 'Senha inválida, por favor preencha todos os campos')
                return render(request, 'paginas/login.html')
            else:
                messages.info(request, 'Usuário e/ou senha incorreto(s)')
                return render(request, 'paginas/login.html')
    else:
        return render(request, 'paginas/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')