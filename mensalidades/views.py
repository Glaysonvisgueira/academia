from django.shortcuts import render,get_object_or_404, redirect


from clientes.models import Cliente
from mensalidades.models import Mensalidade


def listar_mensalidades(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    mensalidades = Mensalidade.objects.filter(cliente=id)
    context = {
    'cliente':cliente,
    'mensalidades': mensalidades,
    }
    template_name = 'mensalidades-pendentes.html'
    return render(request, template_name, context)


def minhas_mensalidades(request):
    mensalidade = Mensalidade.objects.filter(usuario=request.user)
    template_name = 'minhas-mensalidades.html'
    context = {
    	'mensalidade': mensalidade,
    }
    return render(request, template_name, context)


def realizar_pagamento(request):
	return render(request,'pagamento-cartao.html')