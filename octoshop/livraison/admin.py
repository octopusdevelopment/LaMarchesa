from django.contrib import admin
from .models import  Wilaya, Commune
# Register your models here.
admin.site.register(Commune)
admin.site.register(Wilaya)

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'active')
    list_display_links = ('id', 'name')
    list_display_links = ('id','name',)
    list_per_page = 40
    list_editable = ['active']
    list_filter = ('cout',)
    search_fields = ('id', 'name',)