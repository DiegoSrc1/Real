from django import forms
from .models import *
from django.forms import widgets

class Form_Agregar_Productos(forms.ModelForm):
    
    class Meta:
        model = productos
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'inputForm'}),
            'precio' : forms.TextInput(attrs={'class':'inputForm'}),
            'precio_x_mayor' : forms.TextInput(attrs={'class':'inputForm'}),
            'categoria' : forms.TextInput(attrs={'class':'inputForm'}),
            'descripcion' : forms.TextInput(attrs={'class':'inputForm'}),
        }


class contactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
        
class Form_Agregar_Servilletas(forms.ModelForm):

    class Meta:
        model = Servilletas
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'inputForm'}),
        }