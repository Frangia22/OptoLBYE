from optometrialbye.models import Pacientes, Pedidos, Turnos
from django import forms
from optometrialbye.listas import genero_opciones, descripcion_opciones, otra_descripcion, opciones_de_pago, estado
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect, SelectDateWidget
#Llamó a los dinstintos formularios
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
            'genero' : forms.RadioSelect(),
            'historial' : forms.TextInput(attrs={'required': False})
        }


class PedidoForm(forms.ModelForm): 
    class Meta:
        model = Pedidos
        fields = '__all__'
        widgets = {
            'otra_descripcion' : forms.RadioSelect(),
            'pago' : forms.RadioSelect()
        }
        
class TurnoForm(forms.ModelForm): 
    class Meta:
        model = Turnos
        fields = '__all__'   
        widgets = {
            'hora' : forms.DateTimeInput(attrs={'class':'flat'}),
            'dia' : forms.SelectDateWidget()
            
        }   
      