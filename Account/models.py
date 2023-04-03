from django.db import models
from django.contrib.auth.models import User
from App_prosopiki_filosofia.models import Blogcomment


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    nombre = models.CharField(max_length=10)

    descripcion = models.TextField()

    pagina_web = models.URLField()


class UserComment(models.Model):
        blogcomment = models.ForeignKey(Blogcomment, on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

