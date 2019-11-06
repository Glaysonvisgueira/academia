from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from clientes.models import Cliente


UF = (
		('---','---'),
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

STATUS = (
		('---','---'),
        ('ATIVO', 'ATIVO'),
        ('INATIVO', 'INATIVO')        
    )



class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control form-control-sm text-uppercase','onkeypress':'return isNumericKey(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    cpf = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'class':'form-control form-control-sm','onkeypress':'return isNumber(event)', 'autocomplete':'off','placeholder':'000.000.000-00','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    rg = forms.CharField(max_length=14,widget=forms.TextInput(attrs={'class':'form-control form-control-sm','onkeypress':'return isNumber(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    endereco = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class':'form-control form-control-sm text-uppercase','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    complemento = forms.CharField(max_length=150,required=False,widget=forms.TextInput(attrs={'class':'form-control form-control-sm text-uppercase','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    bairro = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control form-control-sm text-uppercase','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    cidade = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control form-control-sm text-uppercase','onkeypress':'return isNumericKey(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    uf = forms.CharField(widget=forms.Select(choices=UF,attrs={'class':'form-control form-control-sm'}))
    nascimento = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'dd/mm/aaaa','class':'form-control form-control-sm','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    telefone = forms.CharField(max_length=12,required=False,widget=forms.TextInput(attrs={'class':'form-control form-control-sm','onkeypress':'return isNumber(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    email = forms.CharField(max_length=70,required=False,widget=forms.TextInput(attrs={'class':'form-control form-control-sm','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    dataInicio = forms.DateField(widget=DatePickerInput(options={"locale":"pt-br"},format='%d/%m/%Y',attrs={'placeholder':'dd/mm/aaaa','class':'form-control form-control-sm','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
    status = forms.CharField(widget=forms.Select(choices=STATUS,attrs={'class':'form-control form-control-sm'}))

    class Meta:
	    model = Cliente
	    fields = ['nome','cpf','rg','endereco','complemento','bairro','cidade','uf','nascimento','telefone','email','dataInicio','status']
