
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<hi>HOLA MUNDO</h1>")

urlpatterns = [
    path('',home),
    path('polls/',include('encuesta.urls')),
    path('admin/', admin.site.urls),
]
