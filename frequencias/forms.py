from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from frequencias.models import Frequencia
from datetime import date


data = date.today()
dia = data.day
mes = data.month 
ano = data.year
dia_atual = str(dia) + '/' + str(mes) + '/' + str(ano)

class FrequenciaForm(forms.ModelForm):
	presente = forms.BooleanField()
	class Meta:
		model = Frequencia
		fields = ['presente']