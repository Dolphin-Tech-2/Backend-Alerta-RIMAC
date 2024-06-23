from django.db import models

# Create your models here.
class Eventos(models.Model):
    latitud = models.FloatField(blank= False, null= False)
    longitud = models.FloatField(blank= False, null= False)
    estado = models.TextField(blank= False, null= False, max_length= 50)
    fecha = models.DateTimeField(auto_now_add= True, blank= True, null= True)
    tipo = models.TextField(blank= False, null= False, max_length= 300)
    color = models.TextField(blank= False, null= False, max_length= 20)
    gemini_output = models.TextField(blank= True, null= True, max_length= 400)

