from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "calzados/home.html")

def hombres(request):
    contexto = {'hombres': Hombres.objects.all()}
    return render(request, "calzados/hombres.html", contexto)

def mujeres(request):
    contexto = {'mujeres': Mujeres.objects.all()}
    return render(request, "calzados/mujeres.html", contexto)


def nenes(request):
    contexto = {'nenes': Nenes.objects.all()}
    return render(request, "calzados/nenes.html", contexto)


def nenas(request):
    contexto = {'nenas': Nenas.objects.all()}
    return render(request, "calzados/nenas.html", contexto)

def hombreForm(request):
    if request.method == "POST":
        miForm = HombreForm(request.POST)
        if miForm.is_valid():
            hombre_nombre = miForm.cleaned_data.get("nombre")
            hombre_descripcion = miForm.cleaned_data.get("descripcion")
            hombre_talle = miForm.cleaned_data.get("talle")
            hombre_precio = miForm.cleaned_data.get("precio")
            hombre_color = miForm.cleaned_data.get("color")
            hombre_material = miForm.cleaned_data.get("material")
            hombre_fecha_Exposicion = miForm.cleaned_data.get("fecha_Exposicion")
            hombre_email = miForm.cleaned_data.get("email")
            hombre = Hombres(nombre=hombre_nombre, descripcion= hombre_descripcion, talle=hombre_talle, precio=hombre_precio, color=hombre_color, material=hombre_material, fecha_Exposicion=hombre_fecha_Exposicion, email=hombre_email)
            hombre.save()
            return render(request, "calzados/home.html")

    else:    
        miForm = HombreForm()

    return render(request, "calzados/hombreForm.html", {"form": miForm })

def mujerForm(request):
    if request.method == "POST":
        miForm = MujerForm(request.POST)
        if miForm.is_valid():
            mujer_nombre = miForm.cleaned_data.get("nombre")
            mujer_descripcion = miForm.cleaned_data.get("descripcion")
            mujer_talle = miForm.cleaned_data.get("talle")
            mujer_precio = miForm.cleaned_data.get("precio")
            mujer_color = miForm.cleaned_data.get("color")
            mujer_material = miForm.cleaned_data.get("material")
            mujer_fecha_Exposicion = miForm.cleaned_data.get("fecha_Exposicion")
            mujer_email = miForm.cleaned_data.get("email")
            mujer = Mujeres(nombre=mujer_nombre, descripcion= mujer_descripcion, talle=mujer_talle, precio=mujer_precio, color=mujer_color, material=mujer_material, fecha_Exposicion=mujer_fecha_Exposicion, email=mujer_email)
            mujer.save()
            return render(request, "calzados/home.html")

    else:    
        miForm = MujerForm()

    return render(request, "calzados/mujerForm.html", {"form": miForm })

def neneForm(request):
    if request.method == "POST":
        miForm = NeneForm(request.POST)
        if miForm.is_valid():
            nene_nombre = miForm.cleaned_data.get("nombre")
            nene_descripcion = miForm.cleaned_data.get("descripcion")
            nene_talle = miForm.cleaned_data.get("talle")
            nene_precio = miForm.cleaned_data.get("precio")
            nene_color = miForm.cleaned_data.get("color")
            nene_material = miForm.cleaned_data.get("material")
            nene_fecha_Exposicion = miForm.cleaned_data.get("fecha_Exposicion")
            nene_email = miForm.cleaned_data.get("email")
            nene = Nenes(nombre=nene_nombre, descripcion= nene_descripcion, talle=nene_talle, precio=nene_precio, color=nene_color, material=nene_material, fecha_Exposicion=nene_fecha_Exposicion, email=nene_email)
            nene.save()
            return render(request, "calzados/home.html")

    else:    
        miForm = NeneForm()

    return render(request, "calzados/neneForm.html", {"form": miForm })

def nenaForm(request):
    if request.method == "POST":
        miForm = NenaForm(request.POST)
        if miForm.is_valid():
            nena_nombre = miForm.cleaned_data.get("nombre")
            nena_descripcion = miForm.cleaned_data.get("descripcion")
            nena_talle = miForm.cleaned_data.get("talle")
            nena_precio = miForm.cleaned_data.get("precio")
            nena_color = miForm.cleaned_data.get("color")
            nena_material = miForm.cleaned_data.get("material")
            nena_fecha_Exposicion = miForm.cleaned_data.get("fecha_Exposicion")
            nena_email = miForm.cleaned_data.get("email")
            nena = Nenas(nombre=nena_nombre, descripcion= nena_descripcion, talle=nena_talle, precio=nena_precio, color=nena_color, material=nena_material, fecha_Exposicion=nena_fecha_Exposicion, email=nena_email)
            nena.save()
            return render(request, "calzados/home.html")

    else:    
        miForm = NenaForm()

    return render(request, "calzados/nenaForm.html", {"form": miForm })

def buscar(request):
    return render(request, "calzados/buscar.html")

def buscarHombres(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        hombres = Hombres.objects.filter(nombre__icontains=patron)
        contexto = {"hombres": hombres }
        return render(request, "calzados/hombres.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")