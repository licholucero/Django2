from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.nombre)

class Direccion(models.Model):
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.calle)

class Proveedor(models.Model):
    rut = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    web = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.nombre)