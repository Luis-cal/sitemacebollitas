# Generated by Django 3.1.1 on 2020-10-06 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_product_porcentaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Porcentaje',
        ),
    ]
