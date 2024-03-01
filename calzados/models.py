from django.db import models
from django.contrib.auth.models import User

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
    
    class Meta:
        verbose_name = "un Nombre de Hombres"
        verbose_name_plural = "Hombres"
    
    def __str__(self):
        return f"{self.nombre}"

class Mujeres(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()
    
    class Meta:
        verbose_name = "un Nombre de Mujeres"
        verbose_name_plural = "Mujeres"
    
    def __str__(self):
        return f"{self.nombre}"
    
class Nenes(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()
    
    class Meta:
        verbose_name = "un Nombre de Nenes"
        verbose_name_plural = "Nenes"
    
    def __str__(self):
        return f"{self.nombre}"

class Nenas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    talle = models.IntegerField()
    precio = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=50)
    fecha_Exposicion = models.DateField()
    email = models.EmailField()
    
    class Meta:
        verbose_name = "un Nombre de Nenas"
        verbose_name_plural = "Nenas"
    
    def __str__(self):
        return f"{self.nombre}"
    
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"     