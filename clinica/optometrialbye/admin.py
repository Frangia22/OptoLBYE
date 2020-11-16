from django.contrib import admin
from optometrialbye.models import Pacientes, Turnos, Pedidos

# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pacientes, PacientesAdmin)
@admin.register(Turnos)
class TurnosAdmin(admin.ModelAdmin):
    pass
@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    pass

