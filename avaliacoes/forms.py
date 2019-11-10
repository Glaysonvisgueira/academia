from django import forms
from avaliacoes.models import Avaliacao, Criterio


CRITERIO = (
	('EQUIPAMENTOS','EQUIPAMENTOS'),
	('ATENDIMENTO','ATENDIMENTO'),
	('INSTRUTORES','INSTRUTORES'),
	('AMBIENTE','AMBIENTE'),
	)

NOTAS = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	)

class AvaliacaoForm(forms.ModelForm):
	is_avaliado = forms.BooleanField(required=True,initial=True)
	notaCriterio1 = forms.CharField(widget=forms.RadioSelect(choices=NOTAS))
	notaCriterio2 = forms.CharField(widget=forms.RadioSelect(choices=NOTAS))
	notaCriterio3 = forms.CharField(widget=forms.RadioSelect(choices=NOTAS))
	notaCriterio4 = forms.CharField(widget=forms.RadioSelect(choices=NOTAS))
	comentario = forms.CharField(required=False,max_length=200,widget=forms.Textarea(attrs={'placeholder':'Insira comentários com sugestões ou críticas...','class':'form-control form-control-sm text-uppercase','onkeypress':'return isNumericKey(event)', 'autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false'}))
	criterio1 = forms.ModelChoiceField(queryset=Criterio.objects.filter(criterio='AMBIENTE'),initial='AMBIENTE')
	criterio2 = forms.ModelChoiceField(queryset=Criterio.objects.filter(criterio='EQUIPAMENTOS'),initial='EQUIPAMENTOS')
	criterio3 = forms.ModelChoiceField(queryset=Criterio.objects.filter(criterio='INSTRUTORES'),initial='INSTRUTORES')
	criterio4 = forms.ModelChoiceField(queryset=Criterio.objects.filter(criterio='ATENDIMENTO'),initial='ATENDIMENTO')

	class Meta:
	    model = Avaliacao
	    fields = ['is_avaliado','notaCriterio1','notaCriterio2','notaCriterio3','notaCriterio4','comentario','criterio1','criterio2','criterio3','criterio4']
