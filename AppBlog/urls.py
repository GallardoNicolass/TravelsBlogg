from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("posts/", posts, name="posts"),
    path("inicio/", inicio, name="inicio"),
    path("perfil/", perfil, name="perfil"),
    path("about/", about, name="about"),

    path("postFormulario/", postFormulario, name="postFormulario"),
    path("busquedaAutor/", busquedaAutor, name="busquedaAutor"),
    path("buscar/", buscar, name="buscar"),
    
    
    
    path("leerPosts/", leerPosts, name="leerPosts"),
    path("eliminarPost/<id>", eliminarPost, name="eliminarPost"),
    path("editarPost/<id>", editarPost, name="editarPost"),

    path("", login_request, name="login"),
    path("register/", register, name="register"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    

]