from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    titulo= models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=150)
    cuerpo= RichTextField(blank=True, null=True)
    autor= models.CharField(max_length=50)
    fecha= models.DateField()
    imagen = models.ImageField(upload_to="imgs")

    def __str__(self):
        return self.titulo
