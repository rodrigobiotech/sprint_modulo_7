from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Tareas(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente','Pendiente'),
        ('En Progreso','En Progreso'),
        ('Completada','Completada'),
        ('Cancelada', 'Cancelada')
    ]
        
    ETIQUETA_CHOICES = [
        ('Trabajo','Trabajo'),
        ('Hogar','Hogar'),
        ('Estudio','Estudio'),
    ]

    PRIORIDAD_CHOICES = [
        ('Baja','Baja'),        
        ('Media','Media'),        
        ('Alta','Alta'),        
        ('Crítica','Crítica'),        
    ]

    
    titulo = models.CharField(max_length=45)
    descripcion = models.TextField(max_length=255)
    fecha_vencimiento = models.DateTimeField()
    estado = models.CharField(max_length=30, choices=ESTADO_CHOICES)
    etiqueta = models.CharField(max_length=30, choices=ETIQUETA_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observacion = models.TextField(max_length=255, null=True)
    prioridad = models.CharField(max_length=40,choices=PRIORIDAD_CHOICES)
    

