# Generated by Django 5.0.6 on 2024-07-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_stock_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(default='Und', max_length=50, verbose_name='Unidad de medida'),
        ),
    ]
