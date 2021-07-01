from django.shortcuts import render, redirect
from django.template import loader
from .models import Libro
from .forms import LibroFormulario



def home(request):
    return render(request, 'core/home.html')

def registro(request):
    libros = Libro.objects.all()

    datos ={
        'libros': libros
    }
    return render(request, 'core/registro_Libro.html',datos)

def mk_libro(request):
    datos = {
        'form': LibroFormulario()
    }

    if request.method == 'POST':
        formulario = LibroFormulario(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos ["mensaje"] = "Guardado Correctamente";
    return render(request, 'core/mk_libro.html', datos)

def mod_libro(request, id):
    libro = Libro.objects.get(Isbn=id)

    datos ={
        'form': LibroFormulario(instance=libro)
    }
    if request.method=='POST':
        formulario = LibroFormulario(data=request.POST,instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']= "Modificado Correctamente"

    return render(request, 'core/mod_libro.html', datos)

def delete_libro(request, id):
    libro = Libro.objects.get(Isbn=id)
    libro.delete()
    return redirect(to=registro)

def reg_user(request):
    
    return render(request, 'core/registro_Usuario.html')


