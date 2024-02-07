from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('hombres/', hombres, name="hombres"),
    path('mujeres/', mujeres, name="mujeres"),
    path('nenes/', nenes, name="nenes"),
    path('nenas/', nenas, name="nenas"),
    
    path('hombre_form/', hombreForm, name="hombre_form"),
    path('mujer_form/', mujerForm, name="mujer_form"),
    path('nene_form/', neneForm, name="nene_form"),
    path('nena_form/', nenaForm, name="nena_form"),
    
    path('buscar/', buscar, name="buscar"),
    path('buscarHombres/', buscarHombres, name="buscarHombres"),

]

