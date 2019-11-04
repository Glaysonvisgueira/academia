from django.contrib import admin

	
from mensalidades.models import Mensalidade 


class MensalidadeAdmin(admin.ModelAdmin):

	list_display = ['id','ano','mes','valor','status','cliente']
	search_fields =['id','ano','mes','valor','status','cliente']	

admin.site.register(Mensalidade, MensalidadeAdmin)
