from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la categoria', max_length = 100, null= False, blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add=True)

    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre', max_length = 100, null= False, blank= False)
    apellido = models.CharField('Apellido', max_length = 100, null= False, blank= False)
    github = models.URLField('GitHub', null= True, blank= True)
    email = models.EmailField('Correo Electronico', null = False, blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nombre +" "+self.apellido

class Post(models.Model):
    id = models.AutoField(primary_key= True)
    titulo = models.CharField('Titulo', max_length=90, blank= False, null= False)
    slug = models.CharField('Slug', max_length=100, blank= False, null= False)
    descripcion = models.CharField('Descripcion', max_length=255, blank=False, null= False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=50000, blank=False, null= False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    estado = models.BooleanField('Publicacion Activada/Publicacion no Activa', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.titulo
    