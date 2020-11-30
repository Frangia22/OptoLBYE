from django.shortcuts import render
from optometrialbye.models import Pacientes, Turnos, Pedidos
from optometrialbye.forms import PacienteForm, PedidoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import logging

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
def index (request):
    return render(request, "optolbye/index.html")
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
def logout_view(request):
    pass
def DetallePaciente (request):
    pacientes = Pacientes.objects.all()
    return render(request, "optolbye/detalle_paciente.html", {"pacientes" : pacientes})

def DetallePedido (request):
    pedidos = Pedidos.objects.all()
    return render(request, "optolbye/detalle_pedido.html", {"pedidos" : pedidos})

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