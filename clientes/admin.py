from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):

	list_display = ['id','user','cpf','rg','nome','email','dataInicio','status']
	search_fields =['id','user','cpf','rg','nome','email','dataInicio','status']	

admin.site.register(Cliente, ClienteAdmin)