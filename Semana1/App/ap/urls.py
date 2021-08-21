
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a mi calculadora :)</h1>")

urlpatterns = [
    path('',home),
    path('Sumar/',include('Sumar.urls')),
    path('admin/', admin.site.urls),
]