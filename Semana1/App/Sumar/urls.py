from django.urls import path

from . import views

urlpatterns = [
    #localhost:8000/Sumar  
    path('',views.index,name='El saludo'),
    #sumando 
    path('<int:numero1>/<int:numero2>',views.Sumando,name='sumando'),
]