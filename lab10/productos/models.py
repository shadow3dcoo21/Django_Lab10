from django.db import models

class productos(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
# Create your models here.
