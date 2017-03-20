from django.contrib import admin

# Register your models here.
from core.models import Pessoa, Cliente

admin.site.register(Pessoa)
admin.site.register(Cliente)