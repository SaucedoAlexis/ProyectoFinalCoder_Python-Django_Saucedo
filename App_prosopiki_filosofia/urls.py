
from django.urls import path
from App_prosopiki_filosofia.views import home

urlpatterns = [
    path('', home, name='InicioProsopiki')
]