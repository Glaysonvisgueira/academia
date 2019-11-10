from django.contrib import admin
	
from avaliacoes.models import Avaliacao, Criterio 


class AvaliacaoAdmin(admin.ModelAdmin):

	list_display = ['id','is_avaliado','avaliador','criterio1','notaCriterio1','criterio2','notaCriterio2','criterio3','notaCriterio3','criterio4','notaCriterio4','comentario','created_at']
	search_fields =['id','is_avaliado','notaCriterio1','notaCriterio2','notaCriterio3','notaCriterio4','comentario','criterio1','criterio2','criterio3','criterio4','avaliador','created_at']	

admin.site.register(Avaliacao, AvaliacaoAdmin)


class CriterioAdmin(admin.ModelAdmin):

	list_display = ['id','criterio']
	search_fields =['id','criterio']	

admin.site.register(Criterio, CriterioAdmin)