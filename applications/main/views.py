from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Receta

def test(request):

    recetas = Receta.objects.all()

    return render(request,"prueba.html",{
        "recetas":recetas
    })

