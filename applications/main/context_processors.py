from .models import Categoria

def getCategorias(request):
    categorias = Categoria.objects.all()
    return {'cat':categorias}