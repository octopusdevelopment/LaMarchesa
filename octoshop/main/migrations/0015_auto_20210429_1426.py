# Generated by Django 3.1.5 on 2021-04-29 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210429_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={},
        ),
        migrations.DeleteModel(
            name='Commune',
        ),
        migrations.DeleteModel(
            name='Wilaya',
        ),
    ]
