from django.shortcuts import render
from django.http import HttpResponse

from .models import CanalMensaje, CanalUsuario, Canal


def mensajes_privados(request, username, *args, **kwargs):

    if not request.user.is_authenticated:
        return HttpResponse("prohibido")

    mi_username =request.user.username

    canal, created = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

    if created:
        print("si fue creado")

    
    

    Usuarios_Canal = canal.canalusuario_set.all().values("usuario__username")
    print(Usuarios_Canal)
    mensaje_canal = canal.canalmensaje_set.all()
    print(mensaje_canal.values("texto"))

    return HttpResponse(f"Nuestro Id del Canal - {canal.id}")
