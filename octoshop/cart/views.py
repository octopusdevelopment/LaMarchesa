from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Product, Taille
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages
from coupons.forms import CouponApplyForm

# translation
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
   
    pk = product.pk
    slug = product.slug
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            # override_quantity=cd['override'],
            taille=cd['taille'],
            color =cd['color']
        )
        return redirect('cart:cart_detail')
    else:
        # the_cart = request
        language = get_language()
        couleur = request.POST.get('color')
        taille = request.POST.get('taille')
        if not couleur and not taille:
            messages.error(request, _('veuillez choisir la taille et la couleur de votre choix'))
        if not couleur and taille:
            if (language == 'ar'):
                messages.error(request,"الرجاء اختيار اللون")
            else:
                messages.error(request, _('veuillez choisir une couleur '))

        if not taille and couleur:
            if (language == 'ar'):
                messages.error(request,"الرجاء اختيار القياس")
            else:
                messages.error(request, _('veuillez choisir une taille'))
        return redirect(f'/{language}/produits/{slug}/{pk}')



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    context = {
        'cart': cart,
        'coupon_apply_form': coupon_apply_form
    }
    return render(request, 'cart.html', context)


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    cart.update(product=product, quantity=quantity)
    return redirect('cart:cart_detail')
