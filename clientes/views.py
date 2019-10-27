from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect

from clientes.models import Cliente
from clientes.forms import ClienteForm


def cadastrar_cliente(request):
    context = {}    
    template_name = 'cadastrar-cliente.html'
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/') #TODO criar página de redirecionamento quando o cadastro for efetuado com sucesso.
    else:
        form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)