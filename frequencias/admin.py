from django.contrib import admin

from frequencias.models import Frequencia


class FrequenciaAdmin(admin.ModelAdmin):

	list_display = ['id','usuario','data','is_presente']
	search_fields =['id','usuario','data','is_presente']	

admin.site.register(Frequencia, FrequenciaAdmin)