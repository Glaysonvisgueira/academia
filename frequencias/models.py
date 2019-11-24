from django.db import models
from django.conf import settings

class Frequencia(models.Model):
	id = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, blank=True)
	data = models.DateField('Data da presença', blank = False)
	is_presente = models.BooleanField(default=False, null = True, blank = True)


	class Meta:
		constraints = [
            models.UniqueConstraint(fields=['usuario', 'data'], name='presença do cliente')
        ]
		verbose_name = "Frequência"
		verbose_name_plural = "Frequências"
		ordering = ['id','usuario','data','is_presente']

