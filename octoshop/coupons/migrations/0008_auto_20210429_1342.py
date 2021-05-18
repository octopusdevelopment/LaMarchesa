# Generated by Django 3.1.5 on 2021-04-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0007_coupon_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(verbose_name='Actif'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Code coupon'),
        ),
    ]