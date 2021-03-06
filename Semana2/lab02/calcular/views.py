import math
from django.shortcuts import render
from math import *
# Create your views here.

def index(request):
    context = {
        'titulo' : "Calculadora"
    }
    return render(request, 'calculo/Operaciones.html', context)

def enviar(request):
    oper = request.POST['operacion']
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    rpta = 0
    if oper == 'suma':
        rpta = num1 + num2
    elif oper == 'resta':
        rpta = num1 - num2
    elif oper == 'multiplicacion':
        rpta = num1 * num2
    elif oper == 'division':
        rpta = num1 / num2
    
    context = {
        'titulo' : "Resultado",
        'num1' : num1,
        'num2' : num2,
        'resultado' : '{:.2f}'.format(rpta),
        'operacion' : oper,
    }
    return render(request, 'calculo/R_Operaciones.html', context)

def indexCilindro(request):
    context = {
        'titulo' : "Calculadora de Cilindro"
    }
    return render(request, 'calculo/cilindro.html', context)

def enviarCilindro(request):
    h = int(request.POST['altura'])
    d = int(request.POST['diametro'])
    rpta = pi * math.pow(d/2, 2) * h
    context = {
        'respuesta' : '{:.2f}'.format(rpta)
    }
    return render(request, 'calculo/R_Cilindro.html', context)