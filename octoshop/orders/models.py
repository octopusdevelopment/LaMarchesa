from django.db import models
from livraison.models import Wilaya, Commune
# , CoutLivraison
# Create your models here.
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
    paid        = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'commande N°:  {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order    = models.ForeignKey(Order,related_name='items', verbose_name=("Commande"), on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, verbose_name=("Commande"), on_delete=models.CASCADE)
    price    = models.DecimalField( max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default = 1 )

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

        