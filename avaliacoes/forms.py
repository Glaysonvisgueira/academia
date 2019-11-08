from django import forms
from avaliacoes.models import Avaliacao, Criterio


CRITERIO = (
	('ESCOLHA UM CRITÉRIO PARA AVALIAR','ESCOLHA UM CRITÉRIO PARA AVALIAR'),
	('EQUIPAMENTOS','EQUIPAMENTOS'),
	('ATENDIMENTO','ATENDIMENTO'),
	('INSTRUTORES','INSTRUTORES'),
	('AMBIENTE','AMBIENTE'),
	)

NOTAS = (
	('ESCOLHA UMA NOTA','ESCOLHA UMA NOTA'),
	('0','0'),
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	('8','8'),
	('9','9'),
	('10','10'),
	)

class AvaliacaoForm(forms.ModelForm):
	is_avaliado = forms.BooleanField(required=True,initial=True)
	nota = forms.CharField(widget=forms.Select(choices=NOTAS,attrs={'class':'form-control form-control-sm','onkeypress':'return isNumericKey(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'})) 
	comentario = forms.CharField(required=False,max_length=200,widget=forms.Textarea(attrs={'placeholder':'Insira comentários com sugestões ou críticas...','class':'form-control form-control-sm text-uppercase','onkeypress':'return isNumericKey(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
	criterio = forms.ModelChoiceField(queryset=Criterio.objects.all(),widget=forms.Select(attrs={'class':'form-control form-control-sm'}))
	#criterio = forms.CharField(widget=forms.Select(choices=CRITERIO,attrs={'class':'form-control form-control-sm'}))

	class Meta:
	    model = Avaliacao
	    fields = ['is_avaliado','nota','comentario','criterio']
