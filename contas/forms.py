from django import forms
from funcionarios.models import Funcionario
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



User = get_user_model()


class RegistroForm(UserCreationForm):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
	email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Já existe usuário com este e-mail cadastrado!')
		return email	

	def save(self, commit=True):
		user = super(RegistroForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	

class AlterarSenhaAcesso(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off'}))
    
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false','placeholder':'Insira seu nome de usuário'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','autocomplete':'off','oncopy':'return false','onpaste':'return false','ondrop':'return false','placeholder':'Insira a sua senha'}))

	class Meta:
		model = User
		fields = ['username','password']
'''
class PasswordChangeForm(SetPasswordForm):#TODO consertar alteração de senha.
	old_password = forms.CharField(max_length=150,widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))

	class Meta:
		model = User
		fields = ['old_password','new_password1','new_password2']'''