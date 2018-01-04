from django.db import models

class Usuario (models.Model):
  nombre = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  contrasena = models.CharField(max_length=50)
  correo = models.EmailField(max_length=70)

class Video (models.Model):
  titulo = models.CharField(max_length=50)
  archivo = models.FileField(upload_to='videos/')
  numeroVisto = models.IntegerField(default='0')
  numeroBuscado = models.IntegerField(default='0')
  fecha = models.DateTimeField(auto_now_add=True)
  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
