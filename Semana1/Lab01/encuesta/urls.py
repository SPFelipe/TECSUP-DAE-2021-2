from django.urls import path

from . import views

urlpatterns = [
    #localhost:8000/polls
    path('',views.index,name='index'),
    #localhost:8000/polls/5
    path('<int:pregunta_id>/<int:numero1>',views.detalle,name='detail'),
    #localhost:8000/polls/5/results
    path('<int:pregunta_id>/results',views.resultados,name='results'),
    #Localhost:8000/polls/5/vote
    path('<int:pregunta_id>/vote',views.votar,name='vote')
]
