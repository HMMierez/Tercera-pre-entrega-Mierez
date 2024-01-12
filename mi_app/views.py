from django.shortcuts import render, redirect
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

def insertar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'insertar_autor.html', {'form': form})

def insertar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LibroForm()
    return render(request, 'insertar_libro.html', {'form': form})

def obtener_resultados_de_la_base_de_datos(query):
    # Lógica de búsqueda en la base de datos
    autores = Autor.objects.filter(nombre__icontains=query)
    libros = Libro.objects.filter(titulo__icontains=query)
    return {'autores': autores, 'libros': libros}

def buscar(request):
    query = request.GET.get('query', '')
    resultados = obtener_resultados_de_la_base_de_datos(query)
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})

def home(request):
    return render(request, 'home.html')
