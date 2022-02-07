from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Categoria(models.Model):
    name = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.CharField(max_length=255,verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Receta(models.Model):

    DIFFICULT = (
        ('0','Facil'),
        ('1','Medio'),
        ('2','Dificil')
    )
    
    title = models.CharField(max_length=100,verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='descripcion',null=True,blank=True)
    content = RichTextUploadingField(verbose_name="contenido")
    time_preparation = models.CharField(max_length=100,verbose_name='Tiempo de preparacion',null=True,blank=True)
    image = models.ImageField(default='null',verbose_name="Imagen de presentacion",upload_to='recetas') 
    slug = models.CharField(unique=True,max_length=150,verbose_name='URL')
    difficult = models.CharField("Dificultad",max_length=1,choices=DIFFICULT,null=True,blank=True)
    public = models.BooleanField(verbose_name="¿Visible?",default=True)
    user = models.ForeignKey(User,verbose_name='Usuario',on_delete=models.CASCADE)
    category = models.ManyToManyField(Categoria,verbose_name='Categoria',null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Ultima actualizacion')

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"

    def __str__(self):
        return self.title + " - " + str(self.created_at) 