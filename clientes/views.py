from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect

from clientes.models import Cliente
from clientes.forms import ClienteForm


def is_valid_queryparam(param):
    return param != '' and param is not None 


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


def listar_clientes(request):    
    clientes = Cliente.objects.all().order_by('id') 
    template_name = 'listar-clientes.html'
    pesquisar = request.GET.get('pesquisar_cliente') 
    if is_valid_queryparam(pesquisar):
        clientes = clientes.filter(nome__icontains=pesquisar) #Pesquisar por objetos que contém a string contida na variável pesquisar.
    
    context = {
        'clientes': clientes, 
    }

    return render(request, template_name, context)

def dados_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    context = {
    'cliente':cliente,
    }
    template_name = 'dados-cliente.html'
    return render(request, template_name, context)

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)   
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('http://localhost:8000/cliente/clientes-cadastrados', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar-cliente.html', {'form': form })
