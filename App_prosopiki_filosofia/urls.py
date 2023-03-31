
from django.urls import path
from App_prosopiki_filosofia.views import inicio, sobre_mi, crear_post

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre_mi/', sobre_mi, name='sobreMi'),
    path('crear_post/', crear_post, name='crearPost')
]