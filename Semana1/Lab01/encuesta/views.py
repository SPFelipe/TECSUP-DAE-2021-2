from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Saludos desde la vista encuesta")

def detalle(request, pregunta_id, numero1):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id + "este es el numero %s" % numero1)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultado de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    respuesta = "Estas votando por la pregunta" + str(pregunta_id)
    return HttpResponse(respuesta)

