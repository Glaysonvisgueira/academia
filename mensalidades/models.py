from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User
from clientes.models import Cliente

hoje = date.today()
ano_atual = hoje.year
mes_atual = hoje.month

VALOR_MENSALIDADE = 89.9

STATUS = (
    ('PAGO','PAGO'),
    ('PENDENTE','PENDENTE'),
)

class Mensalidade(models.Model):
    ano = models.CharField('Ano', max_length = 4, blank=False, default = ano_atual)
    mes = models.CharField('Mês', max_length = 2, blank=False, default = mes_atual)
    valor = models.DecimalField(max_digits = 6, decimal_places=2, blank=False, default = VALOR_MENSALIDADE)
    status = models.CharField('Status de pagamento', choices = STATUS, max_length=8, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)