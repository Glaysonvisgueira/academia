from django.contrib import admin

from clientes.models import Cliente


class ClienteAdmin(admin.ModelAdmin):

	list_display = ['id']
	search_fields =['id']	

admin.site.register(Cliente, ClienteAdmin)