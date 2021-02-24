# Generated by Django 3.1.5 on 2021-02-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.CharField(default='h', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='taille',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]