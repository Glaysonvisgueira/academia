from django.db import models

STATUS = (
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO')        
    )

UF = (
        ('PI', 'PI'),
        ('MA', 'MA'),
        ('AC', 'AC'),
        ('AL', 'AL'),
        ('AM', 'AM'),
        ('AP', 'AP'),
        ('BA', 'BA'),
        ('ES', 'ES'),
        ('CE', 'CE'),
        ('GO', 'GO'),
        ('MT', 'MT'),
        ('MS', 'MS'),
        ('MG', 'MG'),
        ('PA', 'PA'),
        ('PB', 'PB'),
        ('PR', 'PR'),
        ('PE', 'PE'),
        ('RJ', 'RJ'),
        ('RN', 'RN'),
        ('RS', 'RS'),
        ('RO', 'RO'),
        ('RR', 'RR'),
        ('SC', 'SC'),
        ('SP', 'SP'),
        ('SE', 'SE'),
        ('TO', 'TO'),
    )

class Cliente(models.Model):
	id = models.AutoField(primary_key=True)
	cpf = models.CharField('CPF:', max_length = 11, blank=False)
	rg = models.CharField('RG:', max_length = 7, blank=False)
	nome = models.CharField('Nome:', max_length = 100, blank=False)
	endereco = models.CharField('Endereço:', max_length = 150, blank=False)
	complemento = models.CharField('Complemento do endereço:', max_length = 150, null=True, blank=True)
	bairro = models.CharField('Bairro:', max_length = 40, blank=False)
	cidade = models.CharField('Cidade:', max_length = 40, blank=False)
	uf = models.CharField('UF:',  choices=UF,max_length = 2, blank=False)
	nascimento = models.DateField('Data de nascimento:', blank = False)
	telefone = models.CharField('Telefone:', max_length = 12, blank=True, null=True)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
	dataInicio = models.DateField('Data de início:', blank = False)
	created_at = models.DateTimeField('Criado em',auto_now_add = True)
	updated_at = models.DateTimeField('Atualizado em',auto_now = True)
	status = models.CharField('Status:', choices=STATUS,max_length = 7, blank=False)
    
	def __str__(self):
		return self.nome
		
	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"
		ordering = ['id','cpf','rg','nome','dataInicio','status']	
