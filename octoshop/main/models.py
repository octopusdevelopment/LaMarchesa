from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
CATEGORIES = (
    ('CH','chaussures'),
    ('SA','sacs'),
    ('AC','accessoires'),
)

STATUS_PRODUIT = (
    ('N', 'Nouveau'),
    ('R', 'Rupture'),
    ('P', 'Promotion'),
    ('S', 'SANS'),
)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Nom catégorie')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    class Meta:
        ordering = ('name',)
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("main:prod-by-cat", args=[self.slug])


class SubCateory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Sous Catégorie")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Sous Catégorie")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Catégorie', related_name="sub_categories")
    class Meta:
        ordering = ('name',)
        verbose_name = 'Sous Catégorie'
        verbose_name_plural = 'sous Catégories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(SubCateory, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("main:prod-by-sub-cat", args=[self.slug])



class Color(models.Model):
    name        = models.CharField(max_length=254, null=True, blank=True, verbose_name='Nom couleur')
    hex_value   = models.CharField(max_length=7, verbose_name= "Valeur hexadécimale")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Couleur"

class Taille(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, verbose_name='Nom taille')
    def __str__(self):
        return self.name

class Product(models.Model):
    name        = models.CharField(max_length=200, db_index=True, verbose_name='Nom produit')
    slug        = models.SlugField(max_length=200, unique=True)
    subCategory = models.ForeignKey(SubCateory, on_delete=models.CASCADE, verbose_name='Sous catégorie')
    image       = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Photo Principale")
    image2      = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Photo Secondaire")
    image3      = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Photo Térciaire")
    color       = models.ManyToManyField(Color, verbose_name='Couleur')
    taille      = models.ManyToManyField(Taille, verbose_name='Taille')
    status      = models.CharField(choices=STATUS_PRODUIT, max_length=1, default='N', blank=True, null=True, verbose_name='Status')
    price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Prix')
    old_price   = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ancien prix',blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Description')
    afficher    = models.BooleanField(default=True, verbose_name='Afficher')
    show_home = models.BooleanField(default=True, verbose_name='Afficher dans l\'accueil')
    created     = models.DateTimeField(auto_now_add=True, verbose_name='CRÉE')
    updated     = models.DateTimeField(auto_now=True, verbose_name='MODIFIÉ')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product-detail", args=[self.slug, self.id])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(Product, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name = "Produit"
        ordering = ['-created']


class Wilaya(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nom wilaya')
    livraison = models.IntegerField(blank=False, default=0, verbose_name='Prix livraison')

    def __str__(self):
        return self.name

class Commune(models.Model):
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Nom commune')

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name        = models.CharField(verbose_name='Nom complet', max_length=100)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    email       = models.EmailField(verbose_name="Email", null=True, blank = True)
    subject     = models.CharField(verbose_name="Sujet", max_length=50, blank=False)
    message     = models.TextField(verbose_name="Message", blank=False, null=False)
    date_sent = models.DateTimeField(verbose_name="Date", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formulaire de Contact'