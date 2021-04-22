from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# translation
from django.utils.translation import gettext_lazy as _

# Create your models here.
CATEGORIES = (
    ('CH',_('chaussures')),
    ('SA',_('sacs')),
    ('AC',_('accessoires')),
)

STATUS_PRODUIT = (
    ('N', _('Nouveau')),
    ('R', _('Rupture')),
    ('P', _('Promotion')),
    ('S', _('SANS')),
)

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Nom catégorie'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    class Meta:
        #ordering = ('name',)
        verbose_name = _('Catégorie')
        verbose_name_plural = _('Catégories')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("main:prod-by-cat", args=[self.slug])

    def get_ordering(self, request):
       return ['name']



class SubCateory(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_("Nom Sous Catégorie"))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug Catégorie"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Catégorie'), related_name="sub_categories")
    class Meta:
        
        verbose_name = _('Sous Catégorie')
        verbose_name_plural = _('Sous Catégories')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(SubCateory, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("main:prod-by-sub-cat", args=[self.slug])

    def get_ordering(self, request):
       return ['name']


class Color(models.Model):
    name        = models.CharField(max_length=254, null=True, blank=True, verbose_name=_('Nom couleur'))
    hex_value   = models.CharField(max_length=7, verbose_name= _("Valeur hexadécimale"))

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Couleur")

class Taille(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True, verbose_name=_('Nom taille'))
    def __str__(self):
        return self.name

class Product(models.Model):
    name        = models.CharField(max_length=200, db_index=True, verbose_name=_('Nom produit'))
    slug        = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))
    subCategory = models.ForeignKey(SubCateory, on_delete=models.CASCADE, verbose_name=_('Sous catégorie'))
    image       = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=_("Photo Principale"))
    image2      = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=_("Photo Secondaire"))
    image3      = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=_("Photo Térciaire"))
    color       = models.ManyToManyField(Color, verbose_name=_('Couleur'))
    taille      = models.ManyToManyField(Taille, verbose_name=_('Taille'))
    status      = models.CharField(choices=STATUS_PRODUIT, max_length=1, default='N', blank=True, null=True, verbose_name=_('Status'))
    price       = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Prix'))
    old_price   = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Ancien prix',blank=True, null=True))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    afficher    = models.BooleanField(default=True, verbose_name=_('Afficher'))
    show_home = models.BooleanField(default=True, verbose_name=_('Afficher dans l\'accueil'))
    created     = models.DateTimeField(auto_now_add=True, verbose_name=_('CRÉE'))
    updated     = models.DateTimeField(auto_now=True, verbose_name=_('MODIFIÉ'))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("main:product-detail", args=[self.slug, self.id])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name +' '+str(self.id))
        return super(Product, self).save(*args, **kwargs)    
    
    class Meta:
        verbose_name = _("Produit")
        #ordering = ['-created']
    
    def get_ordering(self, request):
       return ['-created']


class Wilaya(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('Nom wilaya'))
    livraison = models.IntegerField(blank=False, default=0, verbose_name=_('Prix livraison'))

    def __str__(self):
        return self.name
    


class Commune(models.Model):
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, verbose_name=_('Wilaya'))
    name = models.CharField(max_length=30, verbose_name=_('Nom commune'))

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank = True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=False)
    message     = models.TextField(verbose_name=_("Message"), blank=False, null=False)
    date_sent = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Formulaire de Contact'