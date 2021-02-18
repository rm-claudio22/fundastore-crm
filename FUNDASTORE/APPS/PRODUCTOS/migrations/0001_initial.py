# Generated by Django 3.1.5 on 2021-01-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_nombre', models.CharField(max_length=128)),
                ('pro_precio', models.FloatField()),
                ('pro_stock', models.IntegerField()),
            ],
        ),
    ]
