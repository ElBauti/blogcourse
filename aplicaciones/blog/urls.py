from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name= 'home'),
    path('android/', android, name='generales'),
    path('python/', python, name='programacion'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('java/', java, name='tutoriales'),
    path('web/', web, name='videojuegos'),
    path("<slug:slug>/",detalle , name="detalle_post"), 
]