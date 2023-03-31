from django import forms
from App_prosopiki_filosofia.models import Blog
from django.forms.widgets import DateInput

class BlogForm(forms.ModelForm):

    fecha = forms.DateField(widget=DateInput(attrs={'type': 'date','class': 'my-datepicker'}))
    imagen = forms.ImageField()
    class Meta:
        model = Blog
        fields = ['titulo','subtitulo','cuerpo','autor']

class BusquedaBlogForm(forms.Form):
    id = forms.ModelChoiceField(queryset=Blog.objects.all(), empty_label=None)

    class Meta:
        model = Blog
        fields = ['autor']