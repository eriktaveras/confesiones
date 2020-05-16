from django.db import models

# Create your models here.
class Confesion(models.Model):
    sexos = (
        ('masculino', 'masculino'),
        ('femenino', 'femenino'),
        ('indefinido', 'indefinido')
    )
    nombre = models.CharField(max_length=50)
    edad = models.DecimalField(max_length=2, max_digits=2, decimal_places=0)
    sexo = models.CharField(max_length=10, choices=sexos, default='indefinido')
    contenido = models.TextField(max_length=420)

    def __str__(self):
        return self.nombre



class Comentario(models.Model):
    confesion = models.ForeignKey(Confesion, on_delete=models.CASCADE, related_name='comentario')
    contenido = models.TextField(max_length=420, default='')

    def __str__(self):
        return self.contenido
    




