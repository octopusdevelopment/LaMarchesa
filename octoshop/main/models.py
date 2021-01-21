from django.db import models
from django.urls import reverse
# Create your models here.
CATEGORIES = (
    ('CH','chaussures'),
    ('SA','sacs'),
    ('AC','accessoires'),
)

STATUS_PRODUIT = (
    ('N', 'nouveau'),
    ('R', 'rupture'),
    ('P', 'promotion'),
    ('S', 'SANS'),
)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:prod-by-cat", args=[self.slug])


class SubCateory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=2, choices=CATEGORIES, default='CH')
    class Meta:
        ordering = ('name',)
        verbose_name = 'Sous Catégorie'
        verbose_name_plural = 'sous Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:prod-by-sub-cat", args=[self.slug])



class Color(models.Model):
    hex_value = models.CharField(max_length=7)
    name = models.CharField(max_length=254, null=True, blank=True, verbose_name='nom')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='nom')
    slug = models.SlugField(max_length=200, unique=True)
    subCategory = models.ForeignKey(SubCateory, on_delete=models.CASCADE, verbose_name='sous categorie')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Photo Principale")

    color = models.ManyToManyField(Color)
    status = models.CharField(choices=STATUS_PRODUIT, max_length=1, default='N', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='prix')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ancien prix',blank=True, null=True)

    description = models.TextField(blank=True)
    afficher = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product-detail", args=[self.id, self.slug])
    





class Wilaya(models.Model):
    name = models.CharField(max_length=30)
    livraison = models.IntegerField(blank=False, default=600)

    def __str__(self):
        return self.name

class Commune(models.Model):
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name