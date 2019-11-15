from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def autorizacao_negada(request):
	return render(request,'sem-autorizacao.html')
