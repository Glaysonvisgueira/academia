from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from avaliacoes import views

urlpatterns = [
	path('listar-avaliações/',views.listar_avaliacoes, name="listar_avaliacoes"),
]
