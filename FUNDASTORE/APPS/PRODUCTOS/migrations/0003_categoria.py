# Generated by Django 3.1.5 on 2021-02-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTOS', '0002_producto_pro_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_nombre', models.CharField(max_length=128)),
                ('cat_itbms', models.FloatField()),
            ],
        ),
    ]
