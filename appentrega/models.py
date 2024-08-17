from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre 
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
