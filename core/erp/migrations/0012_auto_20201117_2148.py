# Generated by Django 3.1.1 on 2020-11-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_auto_20201026_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detsale',
            name='cant',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='pui',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True, verbose_name='PU+iva'),
        ),
    ]