from django.db import models

# Create your models here.


#Clase curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    promedio = models.FloatField()

    def __str__(self):
        return self.nombre

