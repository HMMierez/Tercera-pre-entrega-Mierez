from django.urls import path
from .views import home, insertar_autor, insertar_libro, buscar

urlpatterns = [
    path('', home, name='home'),  
    path('insertar_autor/', insertar_autor, name='insertar_autor'),
    path('insertar_libro/', insertar_libro, name='insertar_libro'),
    path('buscar/', buscar, name='buscar'),
]
