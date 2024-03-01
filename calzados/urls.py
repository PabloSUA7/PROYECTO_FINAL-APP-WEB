from django.urls import path, include
from .views import *
from . import views

from .views import login_request, register, logout_request

urlpatterns = [
    path('', home, name="home"),
     path('acerca_de_mi/', views.acerca_de_mi, name='acerca_de_mi'),
    #_______________________________________________________Hombres
    
    path('hombres/', hombres, name="hombres"),
    path('hombre_crear/', createHombre, name="hombreCrear"),
    path('hombre_actualizar/<id_hombre>/', updateHombre, name="hombreActualizar"),
    path('hombre_borrar/<id_hombre>/', deleteHombre, name="hombreBorrar"),
    
    #________________________________________________________Mujeres
    
    path('mujeres/', mujeres, name="mujeres"),
    path('mujer_crear/', createMujer, name="mujerCrear"),
    path('mujer_actualizar/<id_mujer>/', updateMujer, name="mujerActualizar"),
    path('mujer_borrar/<id_mujer>/', deleteMujer, name="mujerBorrar"),
    
    #_______________________________________________________Nenes
    
    path('nenes/', nenes, name="nenes"),
    path('nene_crear/', createNene, name="neneCrear"),
    path('nene_actualizar/<id_nene>/', updateNene, name="neneActualizar"),
    path('nene_borrar/<id_nene>/', deleteNene, name="neneBorrar"),
    
    #________________________________________________________Nenas
    
    path('nenas/', nenas, name="nenas"),
    path('nena_crear/', createNena, name="nenaCrear"),
    path('nena_actualizar/<id_nena>/', updateNena, name="nenaActualizar"),
    path('nena_borrar/<id_nena>/', deleteNena, name="nenaBorrar"),
    
    #____________________________________________________ login, logout, registro
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', logout_request, name='logout'),
    #path('logout/', LogoutView.as_view(template_name="calzados/logout.html"), name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"), 

    path('buscar/', buscar, name="buscar"),
    path('buscarHombres/', buscarHombres, name="buscarHombres"),

]

