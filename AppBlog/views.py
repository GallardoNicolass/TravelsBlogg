from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from AppBlog.forms import *
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from AppBlog.models import Post


@login_required
def posts(request):
    return render(request, "AppBlogg/posts.html")


@login_required
def inicio(request):
    publicaciones = Post.objects.all()
    return render(request, "AppBlogg/inicio.html", {"publicaciones":publicaciones})

@login_required
def perfil(request):
    return render(request, "AppBlogg/perfil.html")

@login_required
def about(request):
    return render(request, "AppBlogg/about.html")

@login_required
def postFormulario(request):
    if request.method=="POST":
        form= PostForm(request.POST, request.FILES)

        if form.is_valid():
            informacion=form.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= informacion["autor"]
            fecha= informacion["fecha"]
            imagen= request.FILES["imagen"]
            post= Post(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            post.save()
            posts=Post.objects.all()
            return render(request, "AppBlogg/posts.html" ,{"posts":posts, "mensaje": "Post subido correctamente"})
        else:
            return render(request, "AppBlogg/PostFormulario.html" ,{"form": form, "mensaje": "Algo salio mal, vuelve a intentar"})

    else:
        formulario= PostForm()
        return render (request, "AppBlogg/PostFormulario.html", {"form": formulario})

@login_required
def busquedaAutor(request):
    return render(request, "AppBlogg/busquedaAutor.html")

@login_required
def buscar(request):
    autor= request.GET["autor"]
    if autor!="":
        posts= Post.objects.get()
        return render(request, "AppBlogg/resultadosBusqueda.html", {"posts": posts})
    else:
        return render(request, "AppBlogg/busquedaAutor.html", {"mensaje": "Ingresa un autor para busacar"})
        

@login_required
def leerPosts(request):
    posts=Post.objects.all()

    return render(request, "AppBlogg/posts.html", {"posts": posts})

@login_required
def eliminarPost(request, id):
    post=Post.objects.get(id=id)
    post.delete()
    posts=Post.objects.all()
    return render(request, "AppBlogg/Posts.html", {"posts": posts, "mensaje": "Post eliminado correctamente"})

@login_required
def editarPost(request, id):
    postt=Post.objects.get(id=id)
    if request.method=="POST":
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            postt.titulo=info["titulo"]
            postt.subtitulo=info["subtitulo"]
            postt.cuerpo=info["cuerpo"]
            postt.autor=info["autor"]
            postt.fecha=info["fecha"]
            postt.imagen=info["imagen"]
            postt.save()
            posts=Post.objects.all()
            return render(request, "AppBlogg/posts.html", {"posts":posts, "mensaje": "post editado correctamente"})
        pass
    else:
        formulario=PostForm(initial={"titulo":postt.titulo, "subtitulo":postt.subtitulo, "cuerpo":postt.cuerpo, "autor":postt.autor, "fecha":postt.fecha, "imagen":postt.imagen})
        return render(request, "AppBlogg/editarPost.html", {"form":formulario, "post":postt})



def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave) 
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppBlogg/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppBlogg/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppBlogg/login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppBlogg/login.html", {"form": form})

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "AppBlogg/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppBlogg/register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "AppBlogg/register.html", {"form": form})


@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppBlogg/perfil.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppBlogg/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppBlogg/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

