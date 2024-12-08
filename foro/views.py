from django.shortcuts import render
from .models import Galeria,juego,tipomercancia,mercancia
from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
# from .forms import ContactForm

def galeria(request):
    Galerias = Galeria.objects.all()
    paginator = Paginator(Galerias, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"foro/Galeria.html",{"page_obj": page_obj})

def juegos(request):
    tipomerc=tipomercancia.objects.all()
    juegoasc=juego.objects.all()
    return render(request,"foro/merch.html",
                  {'tipo':tipomerc,'juego':juegoasc})

def merch(request):
    merchs=mercancia.objects.all()
    tipomerc=tipomercancia.objects.all()
    juegoasc=juego.objects.all()
    return render(request,"foro/merch.html",
                  {'mercancia':merchs,'tipo':tipomerc,'juego':juegoasc})

def tipomercancias(request,category_id):
    tipoMerc=get_object_or_404(tipomercancia,id=category_id)
    juegoasc=juego.objects.all()
    merchs=mercancia.objects.filter(tipomercancias=tipoMerc)
    return render(request,"foro/categoria.html",
                  {'merchs':merchs,'juego':juegoasc,'tipomercancia':tipoMerc})
