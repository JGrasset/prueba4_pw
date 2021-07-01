from django import forms 
from django.forms import ModelForm
from .models import Libro

class LibroFormulario(ModelForm):
    class Meta:
        model = Libro
        fields =['Isbn','nombre','autor','descripcion','categoria',]