from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    titulo= forms.CharField(label="Titulo Post", max_length=100)
    subtitulo= forms.CharField(label="Subtitulo Post", max_length=150)
    cuerpo= forms.CharField(widget=CKEditorWidget())
    autor= forms.CharField(label="Autor Post", max_length=50)
    fecha= forms.DateField(label="Fecha Post")
    imagen= forms.ImageField(label="imagen")


class RegistroUsuarioForm(UserCreationForm):

    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
        

class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}
