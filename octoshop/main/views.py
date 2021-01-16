from django.shortcuts import render , get_object_or_404
from .models import Product, SubCateory
from django.views.generic import TemplateView, ListView
from cart.forms import CartAddProductForm

    

class IndexView(TemplateView):
    template_name = "index.html"

def product_list(request, category_slug = None):
    category= None
    categories = SubCateory.objects.all()
    products = Product.objects.filter(afficher=True)
    if category_slug:
        category = get_object_or_404(SubCateory, slug=category_slug)
        products = products.filter(subCategory = category)

    return render(request,
        'product.html',{
            'category': category,
            'categories' : categories,
            'products' : products,
            # 'product': product,
        }

    )


def productDetail(request, id, slug):

    product = get_object_or_404(Product, id=id, slug=slug, afficher=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'product-detail.html',{ 'product': product, 'cart_product_form': cart_product_form}) 



