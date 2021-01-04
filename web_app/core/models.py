from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=20)

class Inventario(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    precio_compra = models.IntegerField(null=True, blank=True)

class Venta(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.CharField(max_length=100)
    precio_compra = models.IntegerField(null=True, blank=True)
    precio_venta = models.IntegerField(null=True, blank=True)

