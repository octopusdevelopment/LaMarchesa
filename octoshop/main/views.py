from django.shortcuts import render , get_object_or_404
from .models import Product, SubCateory, Category
from django.views.generic import TemplateView, ListView
from cart.forms import CartAddProductForm



class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(afficher=True)
        context["categories"] = Category.objects.all()
        context["access"] = Category.objects.get(id=1)
        context["chauss"] = Category.objects.get(id=2)
        context["sacs"] = Category.objects.get(id=3)
        
        return context


def product_list(request, category_slug=None):
    sous_cat = None
    cat= None
    sous_categories = SubCateory.objects.all()
    products = Product.objects.filter(afficher=True)

    if category_slug:
        try:
            cat = get_object_or_404(Category, slug=category_slug)
            products = products.filter(subCategory__category = cat)
        except:
            print('subactttdfg')
            sous_cat = get_object_or_404(SubCateory, slug=category_slug)
            products = products.filter(subCategory = sous_cat)


    return render(request,
        'product.html',{
            # 'category': sous_cat,
            'sous_categories' : sous_categories,
            'products' : products,
        }
    )


def productDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, afficher=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product-detail.html',{ 'product': product, 'cart_product_form': cart_product_form}) 



