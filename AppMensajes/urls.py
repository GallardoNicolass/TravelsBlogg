from django.urls import path
from .views import (
    
    
    mensajes_privados

)

urlpatterns=[

path("AppMensajes/<str:username>", mensajes_privados)

]