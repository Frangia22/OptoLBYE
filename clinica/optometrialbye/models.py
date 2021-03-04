from django.db import models
from django.urls import reverse
from datetime import date, time, timedelta, datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from optometrialbye.listas import genero_opciones, descripcion_opciones, opciones_de_pago, estado, otra_descripcion
## Clase paciente
class Pacientes(models.Model):
    #Campos tabla
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    genero = models.CharField(max_length= 2, choices= genero_opciones)
    celular_regex = RegexValidator(regex=r'^\+?549?\d{10}$', message = "Número debe ser ingresado en formato '+549XXXXXXXXXX'.")
    celular = models.CharField("Celular", validators=[celular_regex], max_length = 14, unique = True)
    historial = models.CharField( 'Historial', max_length=200, blank= True)
    #Metadata lo ordeno por apellido
    class Meta:
        ordering = ['apellido']

    #Metodos
    def get_absolute_url(self):
        return reverse ('model-detail-view', args=[str(self.historial)])
    def __str__(self):
        nombre_apellido = f'{self.nombre} {self.apellido}'
        return nombre_apellido
##Clase turnos
class Turnos(models.Model):
    #fecha = models.DateField()
    dia = models.DateField(default= date.today)
    hora = models.TimeField(default= timezone.now)
    medico = models.CharField(max_length=255, blank=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    motivo = models.CharField('Motivo', max_length=255, blank=True)

##Defino que lo ordeno por el dia
    class Meta:
        ordering = ['dia']

    def __str__(self):
        return "{}".format(self.dia)
   
    
       
class Pedidos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=100, choices= descripcion_opciones, blank=False, default= 'Cerca')
    otra_descripcion = models.CharField(max_length= 50, choices= otra_descripcion, default= 'Con armazon')
    precio = models.FloatField()
    subtotal = models.FloatField()
    pago = models.CharField(max_length=100, choices= opciones_de_pago, default= 'Efectivo')
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    estado_pedido = models.CharField(max_length=60, choices= estado, default= 'Pendiente')
    
    class Meta:
        ordering = ['paciente']

    def __str__(self):
        return self.estado_pedido