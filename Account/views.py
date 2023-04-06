from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Account.models import UserProfile
from django.contrib.auth.models import User
from Account.forms import UserRegistrerForm, UserEditForm


# Create your views here.
@login_required
def editar_usuario(request):
    user = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST, request.FILES)


        if form.is_valid():

            data = form.cleaned_data

            user.email = data['email']
            user.save()
            try:
                user.userprofile.nombre = data['nombre']
                user.userprofile.descripcion = data['descripcion']
                user.userprofile.pagina_web = data['pagina_web']

                if not data['imagen']:
                    user.userprofile.imagen = user.userprofile.imagen
                else:
                    user.userprofile.imagen = data['imagen']

                user.userprofile.save()
            except:
                if data['imagen']:
                    imagen = data['imagen']
                else:
                    imagen = 'default/No_Avatar.jpg'

                profile = UserProfile(user=user, nombre=data['nombre'], descripcion=data['descripcion'],
                                      pagina_web=data['pagina_web'], imagen=imagen)
                profile.save()


            return redirect('inicio')
        else:
            try:
                form = UserEditForm(initial={
                    'username': user.username,
                    'email': user.email,
                    'imagen': user.userprofile.imagen,
                    'nombre': user.userprofile.nombre,
                    'descripcion': user.userprofile.descripcion,
                    'pagina_web': user.userprofile.pagina_web,

                })
            except:
                form = UserEditForm(initial={
                    'email': user.email})

            context = {
                'form': form,
                'titulo': 'Editar Usuario',
                'accion': 'Editar',
                'msg': 'Error al editar usuario, revise que el password sea correcto'
            }

            return render(request, 'form.html', context=context)

    try:
        form = UserEditForm(initial={
            'username': user.username,
            'email': user.email,
            'imagen': user.userprofile.imagen,
            'nombre': user.userprofile.nombre,
            'descripcion': user.userprofile.descripcion,
            'pagina_web': user.userprofile.pagina_web,

        })
    except:
        form = UserEditForm(initial={
            'email': user.email})

    context = {
        'form': form,
        'titulo': 'Editar Usuario',
        'accion': 'Editar'
    }

    return render(request, 'form.html', context=context)


def login_account(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'],
                                password=data['password'])

            if user:
                login(request, user)

                return redirect("inicio")

    context = {
        "form": AuthenticationForm(),
        'titulo': 'Logearse',
        'accion': 'Logear'
    }

    return render(request, "form.html", context=context)


def register_account(request):
    if request.method == 'POST':

        form = UserRegistrerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accountLogin')
        else:
            context = {
                'form': form,
                'titulo': 'Registrar Cuenta',
                'accion': 'Registrar',
                'msg': 'Registro fallido revise que su password sea correcto'

            }
            return render(request, 'form.html', context=context)

    form = UserRegistrerForm()
    context = {
        'form': form,
        'titulo': 'Registrar Cuenta',
        'accion': 'Registrar'
    }

    return render(request, 'form.html', context=context)

@user_passes_test(lambda user: user.is_authenticated)
def perfil(request):
    usuario = request.user

    return render(request, 'Account/perfil.html', context={'usuario': usuario})

def perfil_ajeno(request,username):
    user = User.objects.get(username=username)

    context = {
        'usuario': user
    }

    return render(request, 'Account/perfil.html', context)
