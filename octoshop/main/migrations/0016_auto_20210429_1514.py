# Generated by Django 3.1.5 on 2021-04-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210429_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='taille',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Nom taille'),
        ),
        migrations.DeleteModel(
            name='TailleTranslation',
        ),
    ]
