from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('paciente/nuevo', views.NuevoPaciente.as_view(), name = 'nuevo_paciente'),
    path('paciente/detalle', views.DetallePaciente, name = 'detalle_paciente'),
    path('pedido/nuevo', views.NuevoPedido.as_view(), name = 'nuevo_pedido'),
    path('pedido/detalle', views.DetallePedido, name = 'detalle_pedido'),
    path('paciente/editar/<int:pk>', views.PacienteUpdate.as_view(), name = 'editar_paciente'),
    path('paciente/eliminar/<int:pk>', views.PacienteDelete.as_view(), name = 'eliminar_paciente'),
    path('pedido/editar/<int:pk>', views.PedidoUpdate.as_view(), name = 'editar_pedido'),
    path('pedido/eliminar/<int:pk>', views.PedidoDelete.as_view(), name = 'eliminar_pedido'),
    path('turno/nuevo', views.NuevoTurno.as_view(), name = 'nuevo_turno'),
    path('turno/detalle', views.DetalleTurno, name = 'detalle_turno'),
    path('turno/editar/<int:pk>', views.TurnoUpdate.as_view(), name = 'editar_turno'),
    path('turno/eliminar/<int:pk>', views.TurnoDelete.as_view(), name = 'eliminar_turno')
]