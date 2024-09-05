from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar_paciente, name='adicionar_paciente'),
]

