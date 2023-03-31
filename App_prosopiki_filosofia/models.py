from django.db import models


# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=20)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='img_post')
