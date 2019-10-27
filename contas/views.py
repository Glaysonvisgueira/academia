from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required 

from contas.forms import RegistroForm, EditarContaForm, PasswordChangeForm

def registrar_conta(request):
	template_name = 'registrar-conta.html'	
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password = form.cleaned_data['password1'])
			login(request, user)
			return redirect('http://localhost:8000/') #Após o registro o usuário é direcionado para a página principal.
	else:
		form = RegistroForm()
	context = {
			'form' : form	
		}
	return render(request, template_name, context)


@login_required 
def editar_conta(request):
    template_name = 'editar-conta.html'
    context = {}
    if request.method == 'POST':
        form = EditarContaForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            form = EditarContaForm(instance = request.user)
            context['success'] = True
    else:
        form = EditarContaForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required 
def alterar_senha(request):
	template_name = 'alterar-senha.html'
	context = {}
	if request.method == 'POST':
		form = PasswordChangeForm(data = request.POST, user = request.user)
		if form.is_valid():
			user = form.save()
			context['success'] = True
	else:
		form = PasswordChangeForm(user = request.user)
		context['form'] = form
	return render(request, template_name, context)
