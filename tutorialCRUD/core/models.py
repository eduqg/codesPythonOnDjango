from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField()
    idade = models.IntegerField()
    ativo = models.BooleanField()

    def __unicode__(self):
        return self.nome

