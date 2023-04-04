

from django.db import models




# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=20)
    fecha = models.DateField()




class Blogimg(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='img_post')

class Blogcomment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    visto = models.BooleanField(default=False)
    comment = models.TextField()
    user_name = models.CharField(max_length=20)