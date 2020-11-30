from django.contrib import admin
from optometrialbye.models import Pacientes, Turnos, Pedidos

# Register your models here.
@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'celular', 'historial', 'genero', 'id')
#admin.site.register(Pacientes, PacientesAdmin)
@admin.register(Turnos)
class TurnosAdmin(admin.ModelAdmin):
    
    list_display = ('dia', 'hora', 'paciente', 'medico', 'motivo')
@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    pass

