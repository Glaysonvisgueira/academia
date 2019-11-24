from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from frequencias import views

urlpatterns = [
    path('realizar-chamada/',views.realizar_chamada, name="realizar_chamada"),    
]
