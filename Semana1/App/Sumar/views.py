from django.shortcuts import render, resolve_url
from django.http import HttpResponse


def index(request):
    return HttpResponse("Saludos desde la vista para sumar")

def Sumando(request, numero1, numero2):
    suma = numero1 + numero2
    return HttpResponse("Primer numero %s." % numero1 + "mas el Segundo numero  %s" % numero2 + " es igual a : %s"  %suma)