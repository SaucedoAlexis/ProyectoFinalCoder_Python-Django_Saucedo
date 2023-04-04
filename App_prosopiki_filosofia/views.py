from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from Account.models import UserComment
from App_prosopiki_filosofia.forms import BlogForm, BusquedaBlogForm, BlogCommentForm
from App_prosopiki_filosofia.models import Blog, Blogimg, Blogcomment


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def sobre_mi(request):
    return render(request, 'prosopiki_filosofia/sobre_mi.html')


@user_passes_test(lambda user: user.is_superuser)
def crear_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            blog = Blog(
                titulo=data['titulo'],
                subtitulo=data['subtitulo'],
                cuerpo=data['cuerpo'],
                autor=data['autor'],
                fecha=data['fecha']
            )
            blog.save()

            imagen = Blogimg(
                blog=blog,
                imagen=data['imagen']
            )
            imagen.save()

            context = {
                'form': BlogForm(),
                'msg': 'OK'
            }
            return render(request, 'prosopiki_filosofia/crear_post.html', context=context)
        else:
            context = {
                'form': BlogForm(),
                'msg': 'NO'
            }
            return render(request, 'prosopiki_filosofia/crear_post.html', context=context)

    context = {
        'form': BlogForm()
    }
    return render(request, 'prosopiki_filosofia/crear_post.html', context=context)


def posteos(request):
    return render(request, 'prosopiki_filosofia/posteos.html')


def todos_los_posteos(request):
    context = {
        'posteos': Blog.objects.all()
    }

    return render(request, 'prosopiki_filosofia/todos_los_posteos.html', context)


def busqueda_post(request):
    form = BusquedaBlogForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        resultados = Blog.objects.filter(autor__icontains=data['autor'],
                                         titulo__icontains=data['titulo'])
        context = {
            'objects': resultados
        }
    return render(request, 'prosopiki_filosofia/lista_encontrados.html', context=context)


def buscar_post(request):
    return render(request, 'prosopiki_filosofia/buscar_post.html', {'form': BusquedaBlogForm()})


def ver_mas(request, id):
    get_post = Blog.objects.get(id=id)

    get_comment = Blogcomment.objects.filter(blog=get_post)

    context = {
        'field': get_post,
        'comments': get_comment,

    }

    return render(request, 'prosopiki_filosofia/ver_mas.html', context=context)


@user_passes_test(lambda user: user.is_superuser)
def editar_post(request, id):
    get_post = Blog.objects.get(id=id)
    get_blogimg = get_post.blogimg
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            get_post.titulo = data['titulo']
            get_post.autor = data['autor']
            get_post.cuerpo = data['cuerpo']
            get_post.subtitulo = data['subtitulo']
            get_post.fecha = data['fecha']

            get_post.save()

            get_blogimg.imagen = data['imagen']
            get_blogimg.save()

            return redirect('posteosTodos')
    context = {
        'id': get_post.id,
        'form': BlogForm(initial={
            'titulo': get_post.titulo,
            'autor': get_post.autor,
            'subtitulo': get_post.subtitulo,
            'cuerpo': get_post.cuerpo,
            'fecha': get_post.fecha,
            'imagen': get_blogimg.imagen
        })
    }
    return render(request, 'prosopiki_filosofia/editar_post.html', context)


@user_passes_test(lambda user: user.is_superuser)
def eliminar_post(request, id):
    get_post = Blog.objects.get(id=id)
    get_post.delete()
    return redirect('posteosTodos')


@user_passes_test(lambda user: user.is_authenticated)
def comentar(request, id):
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Blogcomment(
                blog=blog,
                comment=data['comment'],
                user_name=request.user
            )
            comment.save()
            user_comment = UserComment(blogcomment=comment, user=request.user)
            user_comment.save()
            return redirect('PostCompleto', id=comment.blog_id)
    context = {
        'form': BlogCommentForm()
    }
    return render(request, 'prosopiki_filosofia/FormComentar.html', context)


@user_passes_test(lambda user: user.is_superuser)
def mensajes_en_blogs(request):
    get_posts = Blog.objects.all()
    posts = []
    for post in get_posts:
        for comm in Blogcomment.objects.filter(blog=post):
            if not comm.visto:
                posts.append(post)
                break

    return render(request, 'prosopiki_filosofia/comentarios_post.html', context={
        'blogs': posts
    })


@user_passes_test(lambda user: user.is_superuser)
def marcar_visto(request, id):
    comment = Blogcomment.objects.get(id=id)
    comment.visto = not comment.visto
    comment.save()
    return redirect('PostCompleto', id=comment.blog_id)


@user_passes_test(lambda user: user.is_authenticated and Blogcomment(user))
def borrar_comment(request, id):
    comment = Blogcomment.objects.get(id=id)
    id = comment.blog_id
    comment.delete()
    return redirect('PostCompleto', id=id)


@user_passes_test(lambda user: user.is_authenticated and Blogcomment(id=user.id))
def editar_comment(request, id):
    get_comment = Blogcomment.objects.get(id=id)
    id = get_comment.blog_id
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            get_comment.comment = data['comment']

            get_comment.save()

            return redirect('PostCompleto', id=id)
    context = {
        'id': id,
        'form': BlogCommentForm(initial={
            'comment': get_comment.comment
        })
    }
    return render(request, 'prosopiki_filosofia/FormEditarComment.html', context)


def mis_comentarios(request, id):
    user = request.user
    comments = Blogcomment.objects.filter(blog_id=id)
    user_comments = UserComment.objects.filter(user=user)
    blog_user_comments = []

    for usercomment in user_comments:
        for comment in comments:
            if comment.id == usercomment.blogcomment_id:
                blog_user_comments.append(comment)

    context = {
        'comments': blog_user_comments,

    }
    return render(request, 'prosopiki_filosofia/mis_comentarios.html', context)
