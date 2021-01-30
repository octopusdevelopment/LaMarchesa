from django.contrib import admin
from .models import CoutLivraison, Wilaya, Commune
# Register your models here.
admin.site.register(CoutLivraison)
admin.site.register(Commune)
admin.site.register(Wilaya)
