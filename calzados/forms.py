from django import forms   
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HombreForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=20, required=True)
    material = forms.CharField(max_length=50, required=True)
    fecha_Exposicion = forms.DateField()
    email = forms.EmailField(required=True)
    
class MujerForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=20, required=True)
    material = forms.CharField(max_length=50, required=True)
    fecha_Exposicion = forms.DateField()
    email = forms.EmailField(required=True) 
    
class NeneForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=20, required=True)
    material = forms.CharField(max_length=50, required=True)
    fecha_Exposicion = forms.DateField()
    email = forms.EmailField(required=True) 
    
class NenaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=50, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.CharField(max_length=50, required=True)
    color = forms.CharField(max_length=20, required=True)
    material = forms.CharField(max_length=50, required=True)
    fecha_Exposicion = forms.DateField()
    email = forms.EmailField(required=True) 
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)      
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)        