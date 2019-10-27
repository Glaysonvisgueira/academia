from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):

	list_display = ['id','cpf','rg','nome','email','dataInicio','status']
	search_fields =['id','cpf','rg','nome','email','dataInicio','status']	

admin.site.register(Cliente, ClienteAdmin)