# Generated by Django 3.1.1 on 2020-10-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0009_auto_20201012_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pui',
            field=models.CharField(max_length=100, null=True, verbose_name='PU+Iva'),
        ),
        migrations.AlterField(
            model_name='client',
            name='dni',
            field=models.CharField(max_length=10, verbose_name='Zona'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
    ]
