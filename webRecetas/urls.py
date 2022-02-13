from xml.dom.minidom import Document
from django.contrib import admin
from django.template import base
from django.urls import path, re_path, include
from .settings import local #Cambiar en produccion

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.main.urls')),
    path('ckeditor',include('ckeditor_uploader.urls')),
]

#Config carga imagenes
if local.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(local.MEDIA_URL,document_root=local.MEDIA_ROOT)