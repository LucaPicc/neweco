from django.db import models
from mercado.models import Prod, Mat
from user.models import Entidad, UserCustom

uni = [
    ('Kg','Kilogramos'),
    ('Tn','Toneladas'),
]
t_mov = [
    ('IN','Ingreso'),
    ('SA','Salida'),

]

class StockProd(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    unidad = models.CharField(choices= uni,max_length=2)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

class StockMat(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    mat = models.ForeignKey(Mat, on_delete=models.CASCADE)
    unidad = models.CharField(choices= uni, max_length=2)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

class MovSP(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)
    unidad = models.CharField(choices= uni, max_length=2)
    tipo = models.CharField(choices = t_mov, max_length=2)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

class MovSM(models.Model):
    mat = models.ForeignKey(Mat, on_delete=models.CASCADE)
    user = models.ForeignKey(UserCustom, on_delete=models.CASCADE)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)
    unidad = models.CharField(choices= uni,max_length=2)
    tipo = models.CharField(choices=t_mov,max_length=2)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

class EnvP(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    ent = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    unidad = models.CharField(choices= uni,max_length=2)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

    def __str__(self):
        en = Entidad.objects.get(id = self.ent_id)
        return en.nombre
    

class RecP(models.Model):
    env = models.ForeignKey(EnvP, on_delete=models.CASCADE)
    ent = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recp = models.BooleanField(default = False)
    f_recp = models.DateTimeField( auto_now=True, auto_now_add=False)

    

class EnvM(models.Model):
    mat = models.ForeignKey(Mat, on_delete=models.CASCADE)
    ent = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    fecha = models.DateTimeField( auto_now=False, auto_now_add=True)
    cant = models.DecimalField( max_digits=15, decimal_places=2)

class RecM(models.Model):
    env = models.ForeignKey(EnvM, on_delete=models.CASCADE)
    ent = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recp = models.BooleanField(default = False)
    f_recp = models.DateTimeField( auto_now=True, auto_now_add=False)
   