from django.contrib import admin
	
from funcionarios.models import Funcionario 


class FuncionarioAdmin(admin.ModelAdmin):

	list_display = ['id','cpf','rg','nome','nomeGuerra','email']
	search_fields =['id','cpf','rg','nome','nomeGuerra','email']	

admin.site.register(Funcionario, FuncionarioAdmin)
