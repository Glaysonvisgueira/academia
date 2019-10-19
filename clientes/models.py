from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=65)    
    peso = models.FloatField(max_length=3)