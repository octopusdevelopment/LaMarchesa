from django.shortcuts import render , get_object_or_404
from .models import Category, SubCateory

def category(request):
    categories = Category.objects.all()
    # categorie = get_object_or_404(Category, pk = cat_id)
    # sub_cat = SubCateory.objects.filter(category_id = cat_id )
    return {
            'categories' : categories
        }
    
def sub_category(request):
    category = Category.objects.all()
    for cat in category:
        sub_cat = cat.sub_categories.all()
    return {
        'sub_cat' : sub_cat
    }