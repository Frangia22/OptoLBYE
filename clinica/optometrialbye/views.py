from django.shortcuts import render
from optometrialbye.models import Pacientes, Turnos, Pedidos
from optometrialbye.forms import PacienteForm, PedidoForm, TurnoForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import logging
import datetime

log = logging.getLogger('odo.info')
# Clases para los formularios
class NuevoPaciente(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pacientes
    template_name = 'optolbye/nuevo_paciente.html'
    form_class = PacienteForm
    success_message = 'Los datos de %(nombre_apellido)s fueron guardados correctamente.'
    success_url = reverse_lazy('index')

    def get_initial(self):
        return {'celular':'+549'}
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data, 
            nombre_apellido = self.object.__str__(),
        )
    def form_valid(self, form):
        response = super().form_valid(form)
        log.info(f"Usuario {self.request.user} ha añadido al paciente {self.object.__str__()}")
        return response


# Create your views here.
# View index
def index (request):
    return render(request, "optolbye/index.html")
# Vista login y autenticacion de usuario
def login_view(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        password = request.POST["password"]
        user = authenticate(request, nombre = nombre, password = password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "optolbye/login.html", { "mensaje" : "El nombre de usuario o la clave son incorrectas."})
    return render(request, "optolbye/login.html")
# Cerrar sesión
def logout_view(request):
    pass
# Vista de detalles
def DetallePaciente (request):
    pacientes = Pacientes.objects.all()
    return render(request, "optolbye/detalle_paciente.html", {"pacientes" : pacientes})

def DetallePedido (request):
    pedidos = Pedidos.objects.all()
    return render(request, "optolbye/detalle_pedido.html", {"pedidos" : pedidos})

def DetalleTurno (request):
    turnos = Turnos.objects.all()
    return render(request, "optolbye/detalle_turno.html", {"turnos" : turnos})

# Vistas para la creacion, eliminación y modificación de las distintas instancias
class NuevoPedido(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pedidos
    template_name = 'optolbye/nuevo_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('index')
class PacienteUpdate(UpdateView):
    model = Pacientes
    template_name = 'optolbye/nuevo_paciente.html'
    form_class = PacienteForm
    success_url = reverse_lazy('index')
class PacienteDelete(DeleteView):
    model = Pacientes
    template_name = 'optolbye/eliminar_paciente.html'
    success_url = reverse_lazy('index')
class PedidoUpdate(UpdateView):
    model = Pedidos
    template_name = 'optolbye/nuevo_pedido.html'
    form_class = PedidoForm
    success_url = reverse_lazy('index')
class PedidoDelete(DeleteView):
    model = Pedidos
    template_name = 'optolbye/eliminar_pedido.html'
    success_url = reverse_lazy('index')
class NuevoTurno(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Turnos
    template_name = 'optolbye/nuevo_turno.html'
    form_class = TurnoForm
    success_url = reverse_lazy('index')
class TurnoUpdate(UpdateView):
    model = Turnos
    template_name = 'optolbye/nuevo_turno.html'
    form_class = TurnoForm
    success_url = reverse_lazy('index')
class TurnoDelete(DeleteView):
    model = Turnos
    template_name = 'optolbye/eliminar_turno.html'
    success_url = reverse_lazy('index')

# Muestra el calendario con las distintas reservas    
def CalendarioDetail(request):
    all_events = Turnos.objects.all()
    get_event_types = Turnos.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Turnos.objects.all()
        else:   
            all_events = Turnos.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.paciente, i.hora
            start_date = datetime.datetime.strptime(str(i.dia.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request,'optolbye/calendario.html',context)

    