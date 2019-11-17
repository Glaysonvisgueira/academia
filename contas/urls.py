from django.contrib import admin
from django.urls import path, include
from contas import views
from django.conf.urls import url

#from django.contrib.auth.views import LoginView


urlpatterns = [
	path('cadastre-se/', views.registrar_conta, name='registrar_conta'),
	path('login/', views.login_page, name='login_page'),
	path('logout/', views.logout, name='logout'),
	path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
] 	