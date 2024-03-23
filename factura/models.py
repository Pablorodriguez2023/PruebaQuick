from django.db import models


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    documento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    
    



class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='facturas', on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre_compañia = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    code = models.CharField(max_length=50) 
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)    
    description = models.TextField()
    
    
class ProductoFactura(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    factura = models.ForeignKey(Factura, related_name='productos', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()