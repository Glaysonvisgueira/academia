from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CRITERIO = (
	('EQUIPAMENTOS','EQUIPAMENTOS'),
	('ATENDIMENTO','ATENDIMENTO'),
	('INSTRUTORES','INSTRUTORES'),
	('AMBIENTE','AMBIENTE'),
	)



class Avaliacao(models.Model):
	is_avaliado = models.BooleanField(default=False)
	notaCriterio1 = models.IntegerField(default = 0, blank = False, null = True)
	notaCriterio2 = models.IntegerField(default = 0, blank = False, null = True)
	notaCriterio3 = models.IntegerField(default = 0, blank = False, null = True)
	notaCriterio4 = models.IntegerField(default = 0, blank = False, null = True)
	comentario = models.CharField('Comentario', max_length=200, null = True, blank = True)
	criterio1 = models.ForeignKey('Criterio', on_delete=models.CASCADE,related_name='+', blank=True, null=True)
	criterio2 = models.ForeignKey('Criterio', on_delete=models.CASCADE,related_name='+', blank=True, null=True)
	criterio3 = models.ForeignKey('Criterio', on_delete=models.CASCADE,related_name='+', blank=True, null=True)
	criterio4 = models.ForeignKey('Criterio', on_delete=models.CASCADE,related_name='+', blank=True, null=True)
	#avaliador = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario_avaliador',null=True, blank= False) 
	avaliador = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, unique=True) 
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)


	class Meta:
		verbose_name = "Avaliação"
		verbose_name_plural = "Avaliações"
		ordering = ['is_avaliado','notaCriterio1','notaCriterio2','notaCriterio3','notaCriterio4','comentario','criterio1','criterio2','criterio3','criterio4','avaliador','created_at']



class Criterio(models.Model):
	criterio = models.CharField(choices=CRITERIO, max_length=12, default=None)

	def __str__(self):
		return self.criterio

	class Meta:
		verbose_name = "Critério"
		verbose_name_plural = "Critérios"
		ordering = ['id','criterio']