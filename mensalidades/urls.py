from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from mensalidades import views

urlpatterns = [    
    url(r'^mensalidades-pendentes/matricula-(?P<id>\d+)/$',views.listar_mensalidades, name="listar_mensalidades"),
    url(r'^pagamento/',views.realizar_pagamento, name="realizar_pagamento"),
    path('minhas-mensalidades/', views.minhas_mensalidades, name='minhas_mensalidades'),
    ]

