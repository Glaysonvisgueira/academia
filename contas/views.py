from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as app_logout         #Alteraando o nome da váriavel para não sobrescrever a váriavel built in logout do django
from django.contrib.auth.decorators import login_required 
from contas.forms import RegistroForm, AlterarSenhaAcesso, LoginForm


def login_page(request):
	context = {}
	template_name = 'login-page.html'
	form = LoginForm(request.POST)
	if request.method == "POST":		
		username = request.POST["username"]
		password = request.POST["password"]
		usuario = authenticate(request, username=username, password=password)
		if usuario is not None:
			login(request, usuario)
			return redirect('http://localhost:8000/')
	else:
		form = LoginForm()
	context = {
		'form': form,
	}
	return render(request, template_name, context)


def logout(request):
	app_logout(request)
	return redirect('http://localhost:8000/')

def registrar_conta(request):
	template_name = 'registrar-conta.html'	
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('http://localhost:8000/') #Após o registro o usuário é direcionado para a página principal.
	else:
		form = RegistroForm()
	context = {
			'form' : form	
		}
	return render(request, template_name, context)

def alterar_senha(request):
    if request.method == 'POST':
        form = AlterarSenhaAcesso(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('http://localhost:8000/')
    else:
        form = AlterarSenhaAcesso(request.user)
    return render(request, 'alterar-senha.html', {
        'form': form
    })

