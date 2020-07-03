from django.contrib import admin
from. models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre','telefono',]
    search_fields = ['nombre',]

class ProductoInline(admin.TabularInline):
    model = Producto