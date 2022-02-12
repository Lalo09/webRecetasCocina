from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('receta/<str:slug>',views.receta,name="receta"),
    path('info',views.info,name="info"),
    path('recetas-sencillas',views.receta_sencilla,name="recetas-sencillas"),
    path('buscar/<str:buscar>',views.buscar,name="buscar")
]
