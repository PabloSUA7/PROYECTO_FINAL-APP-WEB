from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth            import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "calzados/home.html")

#______________________________________________________________________________Acerca de mí
@login_required
def acerca_de_mi(request):
    return render(request, "calzados/acerca_de_mi.html")

#___________________________________________________________________________________Hombres

@login_required
def hombres(request):
    contexto = {'hombres': Hombres.objects.all()}
    return render(request, "calzados/hombres.html", contexto)

@login_required
def createHombre(request):
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
            return redirect(reverse_lazy('hombres'))

    else:    
        miForm = HombreForm()

    return render(request, "calzados/hombreForm.html", {"form": miForm })

@login_required
def updateHombre(request, id_hombre):
    hombre = Hombres.objects.get(id=id_hombre)
    if request.method == "POST":
        miForm = HombreForm(request.POST)
        if miForm.is_valid():
            hombre.nombre = miForm.cleaned_data.get('nombre')
            hombre.descripcion = miForm.cleaned_data.get('descripcion')
            hombre.talle = miForm.cleaned_data.get('talle')
            hombre.precio = miForm.cleaned_data.get('precio')
            hombre.color = miForm.cleaned_data.get('color')
            hombre.material = miForm.cleaned_data.get('material')
            hombre.fecha_Exposicion = miForm.cleaned_data.get('fecha_Exposicion')
            hombre.email = miForm.cleaned_data.get('email')
            hombre.save()
            return redirect(reverse_lazy('hombres'))   
    else:
        miForm = HombreForm(initial={
            'nombre': hombre.nombre,
            'descripcion': hombre.descripcion,
            'talle': hombre.talle,
            'precio': hombre.precio,
            'color': hombre.color,
            'material': hombre.material,
            'fecha_Exposicion': hombre.fecha_Exposicion,
            'email': hombre.email,
        })
        
    return render(request, "calzados/hombreForm.html", {'form': miForm})

@login_required
def deleteHombre(request, id_hombre):
    hombre = Hombres.objects.get(id=id_hombre)
    hombre.delete()
    return redirect(reverse_lazy('hombres'))


#___________________________________________________________________________________Mujeres

@login_required
def mujeres(request):
    contexto = {'mujeres': Mujeres.objects.all()}
    return render(request, "calzados/mujeres.html", contexto)

@login_required
def createMujer(request):
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
            return redirect(reverse_lazy('mujeres'))

    else:    
        miForm = MujerForm()

    return render(request, "calzados/mujerForm.html", {"form": miForm })

@login_required
def updateMujer(request, id_mujer):
    mujer = Mujeres.objects.get(id=id_mujer)
    if request.method == "POST":
        miForm = MujerForm(request.POST)
        if miForm.is_valid():
            mujer.nombre = miForm.cleaned_data.get('nombre')
            mujer.descripcion = miForm.cleaned_data.get('descripcion')
            mujer.talle = miForm.cleaned_data.get('talle')
            mujer.precio = miForm.cleaned_data.get('precio')
            mujer.color = miForm.cleaned_data.get('color')
            mujer.material = miForm.cleaned_data.get('material')
            mujer.fecha_Exposicion = miForm.cleaned_data.get('fecha_Exposicion')
            mujer.email = miForm.cleaned_data.get('email')
            mujer.save()
            return redirect(reverse_lazy('mujeres'))   
    else:
        miForm = MujerForm(initial={
            'nombre': mujer.nombre,
            'descripcion': mujer.descripcion,
            'talle': mujer.talle,
            'precio': mujer.precio,
            'color': mujer.color,
            'material': mujer.material,
            'fecha_Exposicion': mujer.fecha_Exposicion,
            'email': mujer.email,
        })
        
    return render(request, "calzados/mujerForm.html", {'form': miForm})

@login_required
def deleteMujer(request, id_mujer):
    mujer = Mujeres.objects.get(id=id_mujer)
    mujer.delete()
    return redirect(reverse_lazy('mujeres'))

#_____________________________________________________________________________________Nenes

@login_required
def nenes(request):
    contexto = {'nenes': Nenes.objects.all()}
    return render(request, "calzados/nenes.html", contexto)

@login_required
def createNene(request):
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
            return redirect(reverse_lazy('nenes'))

    else:    
        miForm = NeneForm()

    return render(request, "calzados/neneForm.html", {"form": miForm })

@login_required
def updateNene(request, id_nene):
    nene = Nenes.objects.get(id=id_nene)
    if request.method == "POST":
        miForm = NeneForm(request.POST)
        if miForm.is_valid():
            nene.nombre = miForm.cleaned_data.get('nombre')
            nene.descripcion = miForm.cleaned_data.get('descripcion')
            nene.talle = miForm.cleaned_data.get('talle')
            nene.precio = miForm.cleaned_data.get('precio')
            nene.color = miForm.cleaned_data.get('color')
            nene.material = miForm.cleaned_data.get('material')
            nene.fecha_Exposicion = miForm.cleaned_data.get('fecha_Exposicion')
            nene.email = miForm.cleaned_data.get('email')
            nene.save()
            return redirect(reverse_lazy('nenes'))   
    else:
        miForm = NeneForm(initial={
            'nombre': nene.nombre,
            'descripcion': nene.descripcion,
            'talle': nene.talle,
            'precio': nene.precio,
            'color': nene.color,
            'material': nene.material,
            'fecha_Exposicion': nene.fecha_Exposicion,
            'email': nene.email,
        })
        
    return render(request, "calzados/neneForm.html", {'form': miForm})

@login_required
def deleteNene(request, id_nene):
    nene = Nenes.objects.get(id=id_nene)
    nene.delete()
    return redirect(reverse_lazy('nenes'))

#_____________________________________________________________________________________Nenas

@login_required
def nenas(request):
    contexto = {'nenas': Nenas.objects.all()}
    return render(request, "calzados/nenas.html", contexto)

@login_required
def createNena(request):
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
            return redirect(reverse_lazy('nenas'))

    else:    
        miForm = NenaForm()

    return render(request, "calzados/nenaForm.html", {"form": miForm })

@login_required
def updateNena(request, id_nena):
    nena = Nenas.objects.get(id=id_nena)
    if request.method == "POST":
        miForm = NenaForm(request.POST)
        if miForm.is_valid():
            nena.nombre = miForm.cleaned_data.get('nombre')
            nena.descripcion = miForm.cleaned_data.get('descripcion')
            nena.talle = miForm.cleaned_data.get('talle')
            nena.precio = miForm.cleaned_data.get('precio')
            nena.color = miForm.cleaned_data.get('color')
            nena.material = miForm.cleaned_data.get('material')
            nena.fecha_Exposicion = miForm.cleaned_data.get('fecha_Exposicion')
            nena.email = miForm.cleaned_data.get('email')
            nena.save()
            return redirect(reverse_lazy('nenas'))   
    else:
        miForm = NenaForm(initial={
            'nombre': nena.nombre,
            'descripcion': nena.descripcion,
            'talle': nena.talle,
            'precio': nena.precio,
            'color': nena.color,
            'material': nena.material,
            'fecha_Exposicion': nena.fecha_Exposicion,
            'email': nena.email,
        })
        
    return render(request, "calzados/nenaForm.html", {'form': miForm})

@login_required
def deleteNena(request, id_nena):
    nena = Nenas.objects.get(id=id_nena)
    nena.delete()
    return redirect(reverse_lazy('nenas'))

#__________________________________________________________________________________Buscar

@login_required
def buscar(request):
    return render(request, "calzados/buscar.html")

@login_required
def buscarHombres(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        hombres = Hombres.objects.filter(nombre__icontains=patron)
        contexto = {"hombres": hombres }
        return render(request, "calzados/hombres.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#___________________________________________________________________________________Login, Logout, Registracion

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            
            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________
            
            return render(request, "calzados/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "calzados/login.html", {"form": miForm })    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "calzados/registro.html", {"form": miForm })  

def logout_request(request):
    logout(request)
    return redirect(reverse_lazy('login')) 

#______________________________________________________________________________Editar perfil de usuario

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "calzados/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "calzados/editarPerfil.html", {"form": form }) 

#_______________________________________________________________________________Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)
            
            # __________borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "calzados/home.html")

    else:    
        form = AvatarForm()

    return render(request, "calzados/agregarAvatar.html", {"form": form }) 

