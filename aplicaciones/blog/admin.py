from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resources_class = CategoriaResources

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('categoria','estado','fecha_creacion',)

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion','github',)
    resources_class = AutorResources


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)