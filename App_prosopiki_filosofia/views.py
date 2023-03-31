from django.shortcuts import render

from App_prosopiki_filosofia.forms import BlogForm
from App_prosopiki_filosofia.models import Blog


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


def sobre_mi(request):
    return render(request, 'prosopiki_filosofia/sobre_mi.html')


def crear_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            blog = Blog(titulo=data['titulo'],
                        subtitulo=data['subtitulo'],
                        cuerpo=data['cuerpo'],
                        autor=data['autor'],
                        fecha=data['fecha'],
                        imagen=data['imagen'])
            blog.save()
            context = {
                'form': BlogForm(),
                'msg': 'OK'
            }
            return render(request, 'prosopiki_filosofia/crear_post.html', context=context)

    context = {
        'form': BlogForm()
    }
    return render(request, 'prosopiki_filosofia/crear_post.html', context=context)

def posteos(request):
    return render(request, 'prosopiki_filosofia/posteos.html')

def todos_los_posteos(request):
    print(Blog.objects.all())
    context = {
        'posteos': Blog.objects.all()
    }
    return render(request, 'prosopiki_filosofia/todos_los_posteos.html')
