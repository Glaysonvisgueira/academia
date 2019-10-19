from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from funcionarios.models import Funcionario

STATUS = (
		('---', '---'),
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO')        
    )

UF = (
		('---', '---'),
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


class FuncionarioForm(forms.ModelForm):
    nome = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    nomeGuerra = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    rg = forms.CharField(max_length=7,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    endereco = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    complemento = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    uf = forms.CharField(widget=forms.Select(choices=UF,attrs={'class':'form-control form-control-sm'}))
    nascimento = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'dd/mm/aaaa','class':'form-control form-control-sm'}))
    telefone = forms.CharField(max_length=12,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email = forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    dataAdmissao = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'dd/mm/aaaa','class':'form-control form-control-sm'}))
    status = forms.CharField(widget=forms.Select(choices=STATUS,attrs={'class':'form-control form-control-sm'}))
   

    class Meta:
	    model = Funcionario
	    fields = ['nome','nomeGuerra','cpf','rg','endereco','complemento','bairro','cidade','uf','nascimento','telefone','email','dataAdmissao','status']
