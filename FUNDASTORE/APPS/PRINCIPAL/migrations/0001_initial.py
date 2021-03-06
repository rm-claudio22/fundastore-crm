# Generated by Django 3.1.5 on 2021-02-11 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('ban_id', models.AutoField(primary_key=True, serialize=False)),
                ('ban_nombre', models.CharField(max_length=128)),
                ('ban_titulo', models.CharField(max_length=128)),
                ('ban_descripcion', models.CharField(max_length=256)),
                ('pro_imagen', models.ImageField(max_length=128, upload_to='banners')),
            ],
        ),
    ]
