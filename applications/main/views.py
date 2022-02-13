from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Categoria, Receta

num_items = 6;

"""
*Pagina de inicio
*URL: /
"""
def home(request):

    recetas = Receta.objects.filter(public=True)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"home.html",{
        "title":"web de recetas",
        "recetas":page_receta
    })

"""
*Pagina de informacion
*URL: /info
*
"""
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
    
    recetas = Receta.objects.filter(difficult=0)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Recetas sencillas",
        "recetas":page_receta
    })

def postres(request):
    
    categoria = get_object_or_404(Categoria, id=1)
    
    recetas = Receta.objects.filter(category=categoria)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Recetas de postres",
        "recetas":page_receta
    })

def comidas(request):
    
    categoria = get_object_or_404(Categoria, id=2)
    
    recetas = Receta.objects.filter(category=categoria)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Recetas de comidas",
        "recetas":page_receta
    })

def bebidas(request):
    
    categoria = get_object_or_404(Categoria, id=3)
    
    recetas = Receta.objects.filter(category=categoria)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Recetas de bebidas",
        "recetas":page_receta
    })

def todas_las_recetas(request):
    
    recetas = Receta.objects.all()
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Todas nuestras recetas",
        "recetas":page_receta
    })

def buscar(request,buscar):
    
    recetas = Receta.objects.filter(Q(title__icontains=buscar) | Q(descripcion__icontains=buscar))
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"buscar.html",{
        "title":"Resultados de: "+buscar,
        "recetas":page_receta
    })

def recetas_por_categoria(request,id):
    
    categoria = get_object_or_404(Categoria, id=id)
    
    recetas = Receta.objects.filter(category=categoria)
    paginator = Paginator(recetas,num_items)

    page = request.GET.get('page')
    page_receta = paginator.get_page(page)

    return render(request,"page.html",{
        "title":"Todas las recetas de "+categoria.name,
        "recetas":page_receta
    })