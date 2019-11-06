from django.db import models

from django.contrib.auth.models import User

CRITERIO = (
	('EQUIPAMENTOS','EQUIPAMENTOS'),
	('ATENDIMENTO','ATENDIMENTO'),
	('INSTRUTORES','INSTRUTORES'),
	('AMBIENTE','AMBIENTE'),
	)


class Avaliacao(models.Model):
	is_avaliado = models.BooleanField(default=False)
	nota = models.IntegerField(default = 0, blank = False, null = False)
	comentario = models.CharField('Comentario', max_length=200, null = True, blank = True)
	criterio = models.ForeignKey('Criterio', on_delete=models.CASCADE)
	avaliador = models.ForeignKey(User, on_delete=models.CASCADE)


class Criterio(models.Model):
	criterio = models.CharField(choices=CRITERIO, max_length=12, default=None)


