from django.contrib import admin
	
from avaliacoes.models import Avaliacao, Criterio 


class AvaliacaoAdmin(admin.ModelAdmin):

	list_display = ['id','nota','comentario','criterio','avaliador']
	search_fields =['id','nota','comentario','criterio','avaliador']	

admin.site.register(Avaliacao, AvaliacaoAdmin)


class CriterioAdmin(admin.ModelAdmin):

	list_display = ['id','criterio']
	search_fields =['id','criterio']	

admin.site.register(Criterio, CriterioAdmin)