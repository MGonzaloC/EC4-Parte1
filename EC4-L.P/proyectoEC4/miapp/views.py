from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def carreras(request):       
    return render( request,'carreras.html')

def crearcarreras(request):   
    return render( request,'crearcarreras.html')

def cursos(request):   
    return render( request,'cursos.html')

def crearcursos(request):    
    return render( request,'crearcursos.html')