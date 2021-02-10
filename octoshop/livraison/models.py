from django.db import models


# class CoutLivraison(models.Model):
#     def __str__(self):
#         return str(self.cout)
# Create your models here.
class Wilaya(models.Model):
    name = models.CharField(max_length=30)
    cout = models.DecimalField( max_digits=10, verbose_name="coût de livraison", decimal_places=2)
    activer = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Commune(models.Model):
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name