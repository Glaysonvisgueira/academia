"""academia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionario/', include('funcionarios.urls')),
    path('contas/', include('contas.urls')),
    path('cliente/', include('clientes.urls')),
    path('frequencias/', include('frequencias.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('cliente/mensalidades/', include('mensalidades.urls')),
    path('',views.home, name="home"),
    path('venha-ate-nos/',views.venha_ate_nos, name="venha_ate_nos"),
    path('autorização-negada/',views.autorizacao_negada, name="autorizacao_negada"),
    
]
