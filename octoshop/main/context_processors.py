# from .category import Cayrgory
from .models import Category
def Category(request, category_slug=None):
    sous_cat = None
    categories = Category.objects.all()
    if category_slug:
        cat = get_object_or_404(Category, slug=category_slug)
        # products = products.filter(subCategory = category)
        products = products.filter(Category = cat)
    return {
            'categories' : sous_categories,
            'products' : products,
        }
    