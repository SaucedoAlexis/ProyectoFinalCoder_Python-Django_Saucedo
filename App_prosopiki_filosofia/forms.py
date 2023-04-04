from django import forms
from App_prosopiki_filosofia.models import Blog, Blogcomment
from django.forms.widgets import DateInput


class BlogForm(forms.ModelForm):
    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date', 'class': 'my-datepicker'}))
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']


class BusquedaBlogForm(forms.Form):
    autor = forms.CharField(min_length=3)
    titulo = forms.CharField(min_length=3, required=False)

class BlogCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)




