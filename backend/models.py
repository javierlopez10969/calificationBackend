from django.db import models

# Create your models here.


#Clase curso
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    promedio = models.FloatField(default=1.0)

    def __str__(self):
        return self.nombre

