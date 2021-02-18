# Generated by Django 3.1.5 on 2021-02-09 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTOS', '0004_producto_pro_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='cat_itbms',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pro_precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
