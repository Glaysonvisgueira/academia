from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):

	list_display = ['id','nome','peso']
	search_fields =['id','nome','peso']	

admin.site.register(Cliente, ClienteAdmin)