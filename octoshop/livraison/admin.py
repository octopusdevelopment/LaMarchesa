from django.contrib import admin
from .models import  Wilaya, Commune
from parler.admin import TranslatableAdmin


# Register your models here.
@admin.register(Wilaya)
class Wilaya(TranslatableAdmin):
    list_display = ['name', 'cout', 'activer']
    list_editable = ['cout', 'activer']

@admin.register(Commune)
class Commune(TranslatableAdmin):
    list_display = ['name', 'Wilaya',]
    list_editable = ['Wilaya',]