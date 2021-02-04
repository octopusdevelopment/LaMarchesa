from django.contrib import admin

# Register your models here.
from .models import Product, SubCateory, Wilaya, Commune, Color, Category, Taille

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCateory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subCategory' , 'price', 'afficher', 'status', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['subCategory', 'created', 'updated']
    list_editable = ['price', 'afficher', 'status']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hex_value']
    list_editable = ['name', 'hex_value']

@admin.register(Taille)
class TailleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']


