
from django.urls import path
from App_prosopiki_filosofia.views import inicio, sobre_mi, crear_post, posteos, todos_los_posteos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre_mi/', sobre_mi, name='sobreMi'),
    path('posteos/crear_post/', crear_post, name='crearPost'),
    path('posteos/', posteos, name='posteos'),
    path('posteos/todos_los_posteos', todos_los_posteos, name='posteosTodos'),
]