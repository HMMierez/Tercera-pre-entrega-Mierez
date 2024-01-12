from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'precio']
