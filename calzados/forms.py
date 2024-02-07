from django import forms   

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
    


