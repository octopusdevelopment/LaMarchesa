from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Product, Taille
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages

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
        couleur = request.POST.get('color')
        taille = request.POST.get('taille')
        print('zaaalma hna !!')
        if not couleur and not taille:
            messages.error(request, 'veuillez choisir la taille et la couleur de votre choix')
        if not couleur and taille:
            messages.error(request, 'veuillez choisir une couleur ')
        if not taille and couleur:
            messages.error(request, 'veuillez choisir une Taille')
        return redirect(f'/produits/{slug}/{pk}')
        # return HttpResponseRedirect(reverse('main:product-detail'))



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True, 'taille': item['taille'], 'color': item['color']})
    #     print('baskets details', list(cart))

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    print('la quantiteee', type(quantity))
    cart.update(product=product, quantity=quantity)
    return redirect('cart:cart_detail')
