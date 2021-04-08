from django.db import models
from livraison.models import Wilaya, Commune
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon

# , CoutLivraison
"""
The coupon is a foreign key that stores the coupon code used, and the discount is the percentage applied with the 
coupon just in case the coupon gets deleted, we will still have a way to retrieve the discount
"""
from main.models import Product
class Order(models.Model):
    
    first_name  = models.CharField(verbose_name="Nom" , max_length=50)
    last_name   = models.CharField(verbose_name="Prenom" , max_length=50)
    addresse    = models.CharField(verbose_name="Adresse" , max_length=250)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    email       = models.EmailField()
    wilaya      = models.ForeignKey(Wilaya, on_delete=models.SET_NULL, null=True, blank=True)
    commune     = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    note        = models.TextField(blank=True, null=True)
    paid        = models.BooleanField(default=False)
    confirmer   = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete= models.SET_NULL)
    delivery    = models.DecimalField( max_digits=10, verbose_name="Coût de Livraison", decimal_places=2, default=0)

    class Meta:
        verbose_name = "Commande"
        ordering = ('-created',)

    def __str__(self):
        return f'commande N°:  {self.id}'
    

    
    def get_discount(self):
        if self.coupon:
            if self.coupon.discount_amount:
                return self.coupon.discount_amount
            else:
                return (self.coupon.discount_percentage / Decimal(100)) \
                * self.get_total_price()
        return Decimal(0)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        total_cost = total_cost - self.get_discount()
        if total_cost < 0:
            total_cost = 0
        return total_cost + self.delivery


class OrderItem(models.Model):
    order    = models.ForeignKey(Order,related_name='items', verbose_name=("Commande"), on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, verbose_name=("Commande"), on_delete=models.CASCADE)
    price    = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default = 1 )
    taille   = models.CharField(max_length=20)
    color   = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

        