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
    path('comidas',views.comidas,name="comidas"),
    path('postres',views.postres,name="postres"),
    path('bebidas',views.bebidas,name="bebidas"),
    path('recetas',views.todas_las_recetas,name="recetas"),
    path('buscar/<str:buscar>',views.buscar,name="buscar"),
    path('categoria/<str:id>',views.recetas_por_categoria,name="categoria")
]