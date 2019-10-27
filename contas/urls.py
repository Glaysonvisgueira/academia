from django.contrib import admin
from django.urls import path, include
from contas import views
from django.conf.urls import url

urlpatterns = [
	path('cadastre-se/', views.registrar_conta, name='registrar_conta'),
	path('editar-conta/', views.editar_conta, name='editar_conta'),
	path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
] 	