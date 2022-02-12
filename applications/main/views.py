from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Receta

num_items = 10;

def home(request):

    recetas = Receta.objects.filter(public=True)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"home.html",{
        "title":"web de recetas",
        "recetas":page_receta
    })

def info(request):
    
    return render(request,"info.html",{
        "title":"Acerca de la web"
    })

def receta(request,slug):

    receta = Receta.objects.get(public=True, slug=slug)

    receta_sugerencia = Receta.objects.order_by('?')[0]

    return render(request,"receta.html",{
        'receta':receta,
        'receta_sugerencia':receta_sugerencia
    })

def receta_sencilla(request):
    
    recetas = Receta.objects.filter(category=2)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Recetas sencillas",
        "recetas":page_receta
    })

def buscar(request,buscar):
    
    recetas = Receta.objects.filter(Q(title__icontains=buscar) | Q(descripcion__icontains=buscar))
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"buscar.html",{
        "recetas":page_receta
    })

