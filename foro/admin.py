from django.contrib import admin
from .models import mercancia,Galeria, juego, tipomercancia

admin.site.register(Galeria)

class tipomercAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class juegosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class mercanciasAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(tipomercancia,tipomercAdmin)
admin.site.register(juego,juegosAdmin)
admin.site.register(mercancia,mercanciasAdmin)