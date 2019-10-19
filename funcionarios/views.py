from django.shortcuts import render,get_object_or_404, redirect

from funcionarios.models import Funcionario
from funcionarios.forms import FuncionarioForm


def cadastro_sucesso(request):
	return render(request,'sucesso-cadastro.html')

def cadastrar_funcionario(request):
    context = {}    
    template_name = 'cadastrar-funcionario.html'
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://localhost:8000/funcionario/funcionario-cadastrado')
    else:
        form = FuncionarioForm()
    context['form'] = form
    return render(request, template_name, context)



def listar_funcionarios(request):    
    funcionarios = Funcionario.objects.all().order_by('id') 
    funcionarios_ativos = Funcionario.objects.filter(status='ATIVO').count()
    funcionarios_inativos = Funcionario.objects.filter(status='INATIVO').count()
    total_funcionarios = Funcionario.objects.all().count()
    template_name = 'listar-funcionarios.html'     
    context = {
        'funcionarios': funcionarios, 
        'funcionarios_ativos': funcionarios_ativos,
        'funcionarios_inativos':funcionarios_inativos, 
        'total_funcionarios': total_funcionarios,     
    }

    return render(request, template_name, context)




def dados_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    context = {
    'funcionario':funcionario,
    }
    template_name = 'dados-funcionario.html'
    return render(request, template_name, context)