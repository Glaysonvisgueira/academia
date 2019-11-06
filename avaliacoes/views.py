from django.shortcuts import render

from avaliacoes.models import Avaliacao, Criterio

def listar_avaliacoes(request):    
    avaliacoes = Avaliacao.objects.all().order_by('nota') 
    template_name = 'listar-avaliacoes.html'
    context = {
        'avaliacoes': avaliacoes, 
    }
    return render(request, template_name, context)