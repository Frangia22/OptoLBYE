from django.contrib import admin
from optometrialbye.models import Pacientes, Turnos, Pedidos

# Register your models here.///Personalizo la vista de la tabla de la BD o que esta en el sitio de administración
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

