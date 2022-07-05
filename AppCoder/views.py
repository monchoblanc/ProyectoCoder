from django.shortcuts import render
from AppCoder.models import Curso 
from django.http import HttpResponse

# Create your views here.
def curso(self):   #es minuscula porq el model es Curso en models.py...
    curso=Curso(nombre='Django', comision=3020) 
    curso.save()
    texto=f'curso creado: {curso.nombre} {curso.comision}'
    return HttpResponse(texto)