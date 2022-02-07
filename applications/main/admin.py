from django.contrib import admin
from . models import Categoria,Receta

admin.site.register(Categoria)

class RecetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at','updated_at','user',)
    
    list_display = (
        'title','created_at','user','public','difficult'
    )

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

    search_fields = ('title',)
    list_filter=('category',)
    filter_horizontal = ('category',)

admin.site.register(Receta,RecetaAdmin)