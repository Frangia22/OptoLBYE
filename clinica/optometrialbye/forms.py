from optometrialbye.models import Pacientes, Pedidos
from django import forms
from optometrialbye.listas import genero_opciones, descripcion_opciones, otra_descripcion, opciones_de_pago, estado
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'


class PedidoForm(forms.ModelForm): 
    class Meta:
        model = Pedidos
        fields = '__all__'
        
       
      