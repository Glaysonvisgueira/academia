from django.db import models

from django.contrib.auth.models import User

CRITERIO = (
	('EQUIPAMENTOS','EQUIPAMENTOS'),
	('ATENDIMENTO','ATENDIMENTO'),
	('INSTRUTORES','INSTRUTORES'),
	('AMBIENTE','AMBIENTE'),
	)
'''
def validar_avaliacao(criterio):
	if Avaliacao.objects.filter(avaliador='glayson').exists():
		raise ValidationError("Já avaliado!")
'''


class Avaliacao(models.Model):
	is_avaliado = models.BooleanField(default=False)
	nota = models.IntegerField(default = 0, blank = False, null = False)
	comentario = models.CharField('Comentario', max_length=200, null = True, blank = True)
	criterio = models.ForeignKey('Criterio', on_delete=models.CASCADE)
	avaliador = models.ForeignKey(User, on_delete=models.CASCADE, default='1') #Verificar campo Unique para avaliações
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)


	class Meta:
		'''unique_together = [
			("criterio", "avaliador"),	
			]'''
		constraints = [
                     models.UniqueConstraint(fields=['criterio', 'avaliador'],name='a')
                     ]
		verbose_name = "Avaliação"
		verbose_name_plural = "Avaliações"
		ordering = ['is_avaliado','nota','comentario','criterio','avaliador','created_at']




class Criterio(models.Model):
	criterio = models.CharField(choices=CRITERIO, max_length=12, default=None)

	def __str__(self):
		return self.criterio

	class Meta:
		verbose_name = "Critério"
		verbose_name_plural = "Critérios"
		ordering = ['id','criterio']