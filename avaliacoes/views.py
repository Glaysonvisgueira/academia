from django.shortcuts import render,get_object_or_404, redirect

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

from avaliacoes.models import Avaliacao, Criterio
from avaliacoes.forms import AvaliacaoForm

from core import views

def avaliacao_realizada(request):
	return render(request,'avaliacao-realizada.html')

@permission_required('avaliacoes.view_avaliacao', login_url=views.autorizacao_negada)
def listar_avaliacoes(request):    
    avaliacoes = Avaliacao.objects.all()
    template_name = 'listar-avaliacoes.html'
    context = {
        'avaliacoes': avaliacoes,
    }
    return render(request, template_name, context)

@permission_required('avaliacoes.add_avaliacao', login_url=views.autorizacao_negada)
def minha_avaliacao(request):    
    avaliacao = Avaliacao.objects.filter(avaliador=request.user)
    template_name = 'minha-avaliacao.html'
    context = {
        'avaliacao': avaliacao,
    }
    return render(request, template_name, context)


@permission_required('avaliacoes.add_avaliacao', login_url=views.autorizacao_negada)
def avaliar_criterio(request):
	context = {}
	template_name = 'avaliar.html'
	user = User.objects.get(id=request.user.id)
	verificar_usuario = Avaliacao.objects.filter(avaliador=user)
	if verificar_usuario.exists():
		return redirect(avaliacao_realizada) #Caso o usuário já exista, significa que uma avaliação já foi realizada.
	if request.method == 'POST':
		form = AvaliacaoForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.avaliador = request.user
			user.save()
			return redirect(listar_avaliacoes)
	else:
		form = AvaliacaoForm()
	context['form'] = form
	return render(request, template_name, context)
'''

def avaliar_criterio(request):
	context = {}
	template_name = 'avaliar.html'
	if request.user.is_authenticated:
		user = User.objects.get(id=request.user.id)
		if request.method == 'POST':
			form = AvaliacaoForm(request.POST)
			if form.is_valid():
				user = form.save(commit=False)
				user.avaliador = request.user
				user.save()
				return redirect(listar_avaliacoes)
		else:
			form = AvaliacaoForm()
	else:
		if request.method == 'POST':
			form = AvaliacaoForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.save()
				return redirect(listar_avaliacoes)
		else:
			form = AvaliacaoForm()
	context['form'] = form
	return render(request, template_name, context)
'''


