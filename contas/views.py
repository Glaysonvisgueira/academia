from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth import logout as app_logout         #Alteraando o nome da váriavel para não sobrescrever a váriavel built in logout do django
from django.contrib.auth.decorators import login_required 
from core import views
from contas.forms import RegistroForm, AlterarSenhaAcesso


def login(request):
	context = {}
	template_name = 'login-page.html'
	form = AuthenticationForm(request.POST)
	if request.method == "POST":
		username = request.POST("username")
		password = request.POST("password")
		usuario = authenticate(request, username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				return redirect(home)
	else:
		form = AuthenticationForm()
	return render(request,template_name,context)


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

'''
@login_required
def alterar_senha(request):
	template_name = 'alterar-senha.html'
	context = {}
	if request.method == 'POST':
		form = AlterarSenhaAcesso(data = request.POST, user = request.user)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('http://localhost:8000/')
	else:
		form = AlterarSenhaAcesso(user=request.user)
	context['form'] = form
	return render(request, template_name, context)


'''
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



'''

def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})'''