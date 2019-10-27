from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from clientes import views

urlpatterns = [    
    path('cadastrar-cliente/',views.cadastrar_cliente, name="cadastrar_cliente"),
    ]