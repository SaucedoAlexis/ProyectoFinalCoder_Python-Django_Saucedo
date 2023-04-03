from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrerForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    nombre = forms.CharField()
    imagen = forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea)
    pagina_web = forms.URLField()

    class Meta:
        model = User
        fields = ['email', 'imagen', 'nombre', 'descripcion', 'pagina_web']