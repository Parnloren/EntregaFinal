from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='appentrega/inicio.html'), name="Logout"),
    path('editar_perfil/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_contrasenia/', views.CambiarContrasenia.as_view(), name="EditarContrasenia"),
]
