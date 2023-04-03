
from django.urls import path
from App_prosopiki_filosofia.views import inicio, sobre_mi, crear_post, posteos, todos_los_posteos, buscar_post, \
    busqueda_post, ver_mas, editar_post, eliminar_post, comentar, mensajes_en_blogs, marcar_visto, borrar_comment, \
    editar_comment, mis_comentarios

urlpatterns = [
    path('', inicio, name='inicio'),
    path('sobre_mi/', sobre_mi, name='sobreMi'),
    path('posteos/crear_post/', crear_post, name='crearPost'),
    path('posteos/', posteos, name='posteos'),
    path('posteos/todos_los_posteos', todos_los_posteos, name='posteosTodos'),
    path('posteos/buscar', buscar_post, name='BuscarPost'),
    path('posteos/buscar/resultados', busqueda_post, name='ResultadosBusquedaPost'),
    path('posteos/todos_los_posteos/ver_mas/<id>', ver_mas, name='PostCompleto'),
    path('posteos/todos_los_posteos/editar_post/<id>', editar_post, name='EditarPost'),
    path('posteos/todos_los_posteos/eliminar_post/<id>', eliminar_post, name='EliminarPost'),
    path('posteos/todos_los_posteos/ver_mas/agregar_comentario/<id>', comentar, name='Comentar'),
    path('mensajes/', mensajes_en_blogs, name='BlogsMensajes' ),
    path('posteos/todos_los_posteos/ver_mas/visto/<id>', marcar_visto, name='Visto'),
    path('posteos/todos_los_posteos/ver_mas/eliminar/<id>', borrar_comment, name='BorrarComentario'),
    path('posteos/todos_los_posteos/ver_mas/editar/<id>', editar_comment, name='EditarComentario'),
    path('posteos/todos_los_posteos/ver_mas/mis_mensajes/<id>', mis_comentarios, name='MisMensajes')

]