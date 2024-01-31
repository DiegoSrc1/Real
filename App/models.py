from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    precio_x_mayor = models.IntegerField()
    categoria = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)  
    imagen = models.ImageField(upload_to="productos",null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Servilletas(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="servilletas")
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField()
    asunto = models.CharField(max_length=20, null=True)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre