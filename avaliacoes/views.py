from django.shortcuts import render,get_object_or_404, redirect

from avaliacoes.models import Avaliacao, Criterio
from avaliacoes.forms import AvaliacaoForm

def listar_avaliacoes(request):    
    avaliacoes = Avaliacao.objects.all().order_by('nota') 
    template_name = 'listar-avaliacoes.html'
    context = {
        'avaliacoes': avaliacoes, 
    }
    return render(request, template_name, context)



def avaliar_criterio(request):
	context = {}
	template_name = 'avaliar.html'
	if request.method == 'POST':
		form = AvaliacaoForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect(listar_avaliacoes)
	else:
		form = AvaliacaoForm()
	context['form'] = form
	return render(request, template_name, context)