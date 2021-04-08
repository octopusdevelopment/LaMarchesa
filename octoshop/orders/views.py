from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .models import OrderItem, Order
from livraison.models import Wilaya, Commune
from django.views.generic import TemplateView
from .forms import OrderCreateForm
from .tasks import order_send_email
from cart.cart import Cart
from coupons.models import Coupon
from django.core import serializers
import json


"""
- Create an Order object using the save() method of the OrderCreateForm form.
- Avoid saving it to the database yet by using commit=False.
- If the cart contains a coupon, store the related coupon and the discount that was applied.
- Save the order object to the database
"""

def order_create(request):
    cart = Cart(request)
    wilayas= Wilaya.objects.all()
    form = OrderCreateForm()

    if request.method == 'POST':
        if len(cart):
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                print('Le formulaire est valid')
                order = form.save(commit=False)
                order.delivery = order.wilaya.price
                if cart.coupon:
                    coupon = Coupon.objects.get(id= cart.coupon.id, stock__gt=0)
                    if coupon: 
                        order.coupon = cart.coupon
                        order.discount_amount = cart.get_discount()
                        coupon.stock = coupon.stock - 1
                        coupon.save()
                order.save()
                products_total = []
                for item in cart:
                    product = item['price'] * item ['quantity']
                    products_total.append(product)
                    
                    OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'], taille=item['taille'], color=item['color'])
                total_price = cart.get_total_price_after_discount()
                cart.clear()
                order_send_email(order)
                context = {'order': order,
                           'products_total': products_total, 
                           'total_price': total_price,
                           }
                return render(request, 'created.html', context)
        else:
            return redirect(reverse('main:index'))
    else:
        form = OrderCreateForm()
    
    return render(request, 'create.html', {'cart':cart, 'form' : form, 'wilayas' : wilayas})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/order-detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    #weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css\\pdf.css')])# ajouter le style plus t ard erreur ???
    weasyprint.HTML(string=html).write_pdf(response)
    return response

def load_communes_json(request):
    try:
        wilaya_id = request.GET.get('wilaya')
        wilaya = Wilaya.objects.filter(id=wilaya_id)
        
        communes = Commune.objects.filter(Wilaya__id=wilaya_id)
        
        context = json.dumps(serializers.serialize('json', communes))
        
        return HttpResponse(context, content_type='application/json')
    except:
        return HttpResponse('', content_type='application/json')
    

def load_wilaya_json(request):
    try:
        wilaya_id = request.GET.get('wilaya')
        wilaya = Wilaya.objects.filter(id=wilaya_id)
        
        context = json.dumps(serializers.serialize('json', wilaya))
        return HttpResponse(context, content_type='application/json')
    except: 
        return HttpResponse('', content_type='application/json')
        
def load_communes(request):
    
    wilaya_id = request.GET.get('wilaya')
        
    communes = Commune.objects.filter(Wilaya__id=wilaya_id)
    
    context = {
        'communes': communes
    }
    return render(request, 'commune_dropdown_list_options.html', context)
       


