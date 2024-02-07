from django.db import models

# Create your models here.
class Hombres(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()

class Mujeres(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()
    
class Nenes(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()

class Nenas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()