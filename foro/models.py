from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Galeria(models.Model): 
    titulo=models.CharField(max_length=100) 
    Description=models.TextField()
    Imagen=models.ImageField()
    creado=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)  

    class meta:
        verbose_name="New" 
        verbose_nameplural="News"
    
    def __str__ (self):
        return self.title



#nuevos xd
class tipomercancia(models.Model):
    name=models.CharField(max_length=100,verbose_name="tipomerc")
    created=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")


    class meta:
        verbose_name="tipoMercancia"
        verbose_name_plural="tipoMercancias"

    def __str__(self):
        return self.name



class juego(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    detail=models.TextField(verbose_name="detalle")
    image=models.ImageField(upload_to="juegos",null=True,blank=True,verbose_name="imagen")
    published=models.DateTimeField(default=now,verbose_name="fecha publicacion")
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="autor")
    tipomercancias=models.ManyToManyField(tipomercancia,verbose_name="Tipo de Mercancia")
    created=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")

    class meta:
            verbose_name="juego"
            verbose_name_plural="juegos"

    def __str__(self):
        return self.name


class mercancia(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    detail=models.TextField(verbose_name="Detalle producto")
    created=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    image=models.ImageField(upload_to="mercancia",null=True,blank=True,verbose_name="imagen")
    tipomercancias=models.ManyToManyField(tipomercancia,verbose_name="Tipo de Mercancia")
    juegosito=models.ManyToManyField(juego,verbose_name="juegos asociados")
    updated=models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")


    class meta:
        verbose_name="Mercancia"
        verbose_name_plural="Mercancias"

    def __str__(self):
        return self.name
