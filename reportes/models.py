from django.db import models

# Create your models here.
#Register Model in ADMIN.PY

class Usuarios(models.Model):
    nombre = models.CharField(max_length =256) 
    email = models.CharField(max_length =256)   
    password = models.CharField(max_length =256)
    puesto = models.CharField(max_length =256)
    fechaAlta = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.puesto

