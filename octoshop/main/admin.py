from django.contrib import admin

# Register your models here.
from .models import Product, SubCateory, Color, Category, Taille, ContactForm
from parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['id', 'name']
    exclude = ['slug',]

@admin.register(SubCateory)
class SubCategoryAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'category']
    exclude = ['slug',]


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'subCategory' , 'price', 'afficher', 'status', 'updated', 'show_home']
    list_filter = ['subCategory', 'created', 'updated']
    list_editable = ['price', 'afficher', 'status','show_home']
    exclude = ['slug',]


@admin.register(Color)
class ColorAdmin(TranslatableAdmin):
    list_display = ['id', 'name', 'hex_value']
    list_editable = ['hex_value']

@admin.register(Taille)
class TailleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# Contact
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'subject', 'date_sent')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')

