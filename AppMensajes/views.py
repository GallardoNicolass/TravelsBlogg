from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import CanalMensaje, CanalUsuario, Canal
from .forms import FormMensajes
from django.views.generic.edit import FormMixin

class CanalFormMixin(FormMixin):
    form_class = FormMensajes
    #success_url = "./"

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        if not  request.user.is_authenticated:
            raise PermissionDenied

        form = self.get_form()
        if form.is_valid():
            canal = self.get_object()
            usuarioo = self.request.user
            mensaje = form.cleaned_data.get("mensaje")
            canal_obj = CanalMensaje.objects.create(canal=canal, usuarioo=usuarioo, texto=mensaje)

            if request.is_ajax():
                return JsonResponse({
                    'mensaje':canal_obj.texto,
                    'username':canal_obj.usuarioo.username
                    }, status=201)
                    
            return super().form_valid(form)

        else:
            if request.is_ajax():
                return JsonResponse({"Error":form.errors}, status=400)

            return super().form_invalid(form)    

class CanalDetailView(LoginRequiredMixin, CanalFormMixin, DetailView):
    template_name= 'AppMensajes/canal_detail.html'
    queryset = Canal.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        obj = context['object']
        print(obj)
        #if self.request.user not in obj.usuarios.all():
         #   raise PermissionDenied

        context['si_canal_miembro'] = self.request.user in obj.usuarios.all()
        return context

    #def get_queryset(self):
     
     #   usuario = self.request.user
     #  username = usuario.username
   # qs = Canal.objects.all().filtrar_por_username(username)
    #return qs 


class DetailMs(LoginRequiredMixin, DetailView):
    template_name= 'AppMensajes/canal_detail.html'
    def get_object(self, *args, **kwargs):

        username = self.kwargs.get("username")
        mi_username = self.request.user.username
        canal, _ = Canal.objects.obtener_o_crear_canal_ms(mi_username, username)

        if username == mi_username:
            mi_canal, _ = Canal.objects.obtener_0_crear_canal_usuario_actual(self.request.user)
            return mi_canal

        if canal == None:
            raise Http404
        return canal


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
