from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib import messages
# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, 'Usuario já cadastrado.')
            return redirect('cadastro')
        user = User.objects.create_user(first_name=nome, last_name=sobrenome, username=username, email=email, password=senha)
        user.save()
        return HttpResponse("Cadastrado com sucesso")


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
    
    user = authenticate(username=username, password=senha)
    if(user):
        login_django(request, user)
        if request.user.is_authenticated:
            return redirect('../plataforma/')
    else:
        messages.info(request, 'Username ou senha inválidos.')
        return redirect('login')

def plataforma(request):
    if request.user.is_authenticated:
        return render(request, 'plataforma.html')
    else:
        messages.info(request, 'Faça o login para usar a plataforma.')
        return redirect('../login/')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi deslogado com sucesso. Até mais!')
    return redirect('../login/')