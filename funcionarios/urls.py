from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from funcionarios import views

urlpatterns = [    
    path('cadastrar-funcionario/',views.cadastrar_funcionario, name="cadastrar_funcionario"),
    path('funcionario-cadastrado/',views.cadastro_sucesso, name="cadastro_sucesso"),   
    path('funcionarios-cadastrados/',views.listar_funcionarios, name="listar_funcionarios"), 
    url(r'^matricula-(?P<id>\d+)/$', views.dados_funcionario, name="dados_funcionario"),
    
    ]