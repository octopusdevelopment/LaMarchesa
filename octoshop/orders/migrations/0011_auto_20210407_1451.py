# Generated by Django 3.1.5 on 2021-04-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20210301_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Coût de Livraison'),
        ),
    ]