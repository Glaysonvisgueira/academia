from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from core import views
from funcionarios.models import Funcionario
from funcionarios.forms import FuncionarioForm


def is_valid_queryparam(param):
    return param != '' and param is not None 

def cadastro_sucesso(request):
	return render(request,'sucesso-cadastro.html')

@permission_required('funcionarios.add_funcionario', login_url=views.autorizacao_negada)
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


@permission_required('funcionarios.view_funcionario', login_url=views.autorizacao_negada)
def listar_funcionarios(request):    
    funcionarios = Funcionario.objects.all().order_by('id') 
    funcionarios_ativos = Funcionario.objects.filter(status='ATIVO').count()
    funcionarios_inativos = Funcionario.objects.filter(status='INATIVO').count()
    total_funcionarios = Funcionario.objects.all().count()
    template_name = 'listar-funcionarios.html'
    pesquisar = request.GET.get('pesquisar_funcionario') 
    if is_valid_queryparam(pesquisar):
        funcionarios = funcionarios.filter(nome__icontains=pesquisar) #Pesquisar por objetos que contém a string contida na variável pesquisar.
        total_funcionarios = funcionarios.filter(nome__icontains=pesquisar).count()
    context = {
        'funcionarios': funcionarios, 
        'funcionarios_ativos': funcionarios_ativos,
        'funcionarios_inativos':funcionarios_inativos, 
        'total_funcionarios': total_funcionarios,     
    }

    return render(request, template_name, context)


@permission_required('funcionarios.can_change_Funcionario', login_url=views.autorizacao_negada)
def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.save()
            return redirect('http://localhost:8000/funcionario/funcionarios-cadastrados', pk=funcionario.pk)
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'editar-funcionario.html', {'form': form })


@permission_required('funcionarios.can_view_Funcionario', login_url=views.autorizacao_negada)
def dados_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    context = {
    'funcionario':funcionario,
    }
    template_name = 'dados-funcionario.html'
    return render(request, template_name, context)


@permission_required('funcionarios.delete_funcionario', login_url=views.autorizacao_negada)
def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()
    return redirect(listar_funcionarios)
