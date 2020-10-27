from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
# Usuario personalizados

class Entidad(models.Model):

    tipo_entity=[
        ('MU','Municipio'),
        ('CO', 'Cooperativa'),
        ('PL', 'Punto Limpio'),
        ('EM', 'Empresa'),
    ]

    nombre = models.CharField(max_length=50, unique = True)
    pais = models.CharField(max_length=250, blank = True, null = True)
    prov = models.CharField('Provincia', max_length=50, blank = True, null = True)
    loc = models.CharField('Localidad', max_length=50, null = True, blank = True)
    tipo = models.CharField(choices = tipo_entity, max_length=2,default = '')

    def __str__(self):
        return self.nombre
    

class UserCustom(AbstractUser):
    entity = models.ForeignKey(Entidad,on_delete=models.CASCADE, null = True)
    is_admin_entity = models.BooleanField(default=False)
    is_user_entity = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)



