from django.db import models


# translation
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Wilaya(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=30, verbose_name=_('Nom Wilaya'),))

    cout = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=_('Coût de Livraison'))
    activer = models.BooleanField(default=True, verbose_name=_('Activer'))
    def __str__(self):
        return self.name

class Commune(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=30, verbose_name=_('Nom Commune')),)
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, verbose_name=_('Wilaya'))
    

    def __str__(self):
        return self.name