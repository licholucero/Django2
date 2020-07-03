from django.contrib import admin
from. models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre','telefono',]
    search_fields = ['nombre',]

class ProductoInline(admin.TabularInline):
    model = Producto






















admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto,)
admin.site.register(Direccion)
admin.site.register(Detalle)
admin.site.register(Venta)