from django.shortcuts import render , get_object_or_404
from .models import Product, SubCateory, Category
from django.views.generic import TemplateView, ListView, CreateView
from cart.forms import CartAddProductForm
from .forms import ContactForm
# shuffle elements catalogue
import random
# pagination
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(afficher=True, show_home=True)
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
    
    paginate_by = 24

    if category_slug:
        try:
            cat = get_object_or_404(Category, slug=category_slug)
            products = products.filter(subCategory__category = cat)
        except:
            sous_cat = get_object_or_404(SubCateory, slug=category_slug)
            products = products.filter(subCategory = sous_cat)
    length = len(products)
    # paginate products
    paginator = Paginator(products, paginate_by)
    page = request.GET.get('page')
    print('page', page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
        print('here')
        print('num pages', paginator.num_pages)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        print('num pages', paginator.num_pages)

    return render(request,
        'product.html',{

            'sous_categories' : sous_categories,
            'products' : products,
            'size': length
        }
    )


def productDetail(request, id, slug):
    
    product = get_object_or_404(Product, id=id, slug=slug, afficher=True)
    similar_products = sorted(Product.objects.filter(subCategory= product.subCategory, afficher=True).exclude(slug=slug)[:4], key=lambda x: random.random())
    cart_product_form = CartAddProductForm()
    return render(request, 'product-detail.html',{ 'product': product, 'cart_product_form': cart_product_form, 'similar_products':similar_products}) 


def aboutView(request):
    return render(request, 'about.html') 

def contactView(request):
    return render(request, 'contact.html') 


class ContactFormView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
  
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
      
        message = 'Une erreur est survenue, veuillez réessayer.'
        success = False
        try:
            #save the form   
            if form.is_valid():
                form.save()
                #messages.success(request, 'Votre message a bien été envoyé')
                message = 'Votre message a bien été envoyé!'
                success = True
                print(success)
                return render(request, 'other/contact.html', {'message': message, 'success': success})
            else:
                print(success)
                message = 'Une erreur est survenue, veuillez réessayer.'
                return render(request, 'contact.html', {'message': message, 'failure': True})
        except:
            return render(request, 'contact.html', {'message': message, 'failure': True})
        return render(request, 'contact.html', {'message': message, 'failure': True})