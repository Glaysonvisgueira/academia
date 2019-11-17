from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def autorizacao_negada(request):    #Página a ser exibida quando o usuário acessar alguma URL não permitida.
	return render(request,'sem-autorizacao.html')
