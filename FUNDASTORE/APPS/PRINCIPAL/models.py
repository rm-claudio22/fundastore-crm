from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    class Categoria(models.TextChoices):
        RECETAS = 'R',_('RECETAS')
        NOTICIAS = 'N',_('NOTICIAS')
    
    blg_id          = models.AutoField(primary_key=True)
    blg_tipo        = models.CharField(max_length=1, choices = Categoria.choices)
    blg_titulo      = models.CharField(max_length=32)
    blg_descripcion = models.CharField(max_length=256)
    blg_banner      = models.ImageField(upload_to="principal/blog/", max_length=256)
    blg_video       = models.URLField()
    blg_post        = HTMLField()
    blg_fecha_post  = models.DateTimeField(auto_now_add=True)
    blg_fecha_act   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blg_titulo


class Banner(models.Model):
    ban_id          = models.AutoField(primary_key=True)
    ban_nombre      = models.CharField(max_length=128)
    ban_titulo      = models.CharField(max_length=128)
    ban_descripcion = models.CharField(max_length=256)
    pro_imagen      = models.ImageField(upload_to='banners',max_length=128)

    def __str__(self):
        return self.ban_nombre