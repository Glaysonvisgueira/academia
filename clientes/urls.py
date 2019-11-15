from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from clientes import views

urlpatterns = [    
    path('cadastrar-cliente/',views.cadastrar_cliente, name="cadastrar_cliente"),
    path('clientes-cadastrados/',views.listar_clientes, name="listar_clientes"),
    path('excluir-cliente/<int:id>',views.excluir_cliente, name="excluir_cliente"),
    url(r'^matricula-(?P<id>\d+)/$', views.dados_cliente, name="dados_cliente"),
    url(r'^editar/matricula-(?P<pk>\d+)/$', views.editar_cliente, name="editar_cliente"),
    ]