from django.urls import path, include

from Account.views import editar_usuario, login_account, register_account, perfil

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', login_account, name='accountLogin'),
    path('logout/', LogoutView.as_view(template_name="account/logout.html"), name='accountLogout'),
    path('registrar/', register_account, name='accountRegister'),
    path('editar/', editar_usuario, name='accountEditar'),
    path('profile/', perfil, name='perfil')

]
