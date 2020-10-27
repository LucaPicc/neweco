from django.db import models
from user.models import Entidad

meses = (
    ('1','Enero'),
    ('2','Febrero'),
    ('3','Marzo'),
    ('4','Abril'),
    ('5','Mayo'),
    ('6','Junio'),
    ('7','Julio'),
    ('8','Agosto'),
    ('9','Septiembre'),
    ('10','Octubre'),
    ('11','Noviembre'),
    ('12','Diciembre'),
)
año=(
        ('2000','2000'),
        ('2001','2001'),
        ('2002','2002'),
        ('2003','2003'),
        ('2004','2004'),
        ('2005','2005'),
        ('2006','2006'),
        ('2007','2007'),
        ('2008','2008'),
        ('2009','2009'),
        ('2010','2010'),
        ('2011','2011'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'),
        ('2016','2016'),
        ('2017','2017'),
        ('2018','2018'),
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
    )
class GIRSU(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recup = models.DecimalField( max_digits=15, decimal_places=2)
    empleos = models.IntegerField()
    g_rec = models.DecimalField( max_digits=15 , decimal_places=2)
    g_girsu = models.DecimalField( max_digits=15, decimal_places=2)
    f_mes = models.CharField(choices=meses, max_length=2)
    f_año = models.CharField(choices=año, max_length=4)

class Empleos(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recolecccion = models.IntegerField()
    clas = models.IntegerField()
    educ = models.IntegerField()
    disp = models.IntegerField()
    f_mes = models.CharField(choices=meses, max_length=2)
    f_año = models.CharField(choices=año, max_length=4)

class Recuperacion(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recol = models.DecimalField( max_digits=15, decimal_places=2)
    clasf = models.DecimalField( max_digits=15, decimal_places=2)
    edu = models.DecimalField( max_digits=15, decimal_places=2)
    f_mes = models.CharField(choices=meses, max_length=2)
    f_año = models.CharField(choices=año,max_length=4)

class GGirsu(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    recoleccion = models.DecimalField( max_digits=15, decimal_places=2)
    gest_reci = models.DecimalField( max_digits=15, decimal_places=2)
    disp_trat = models.DecimalField( max_digits=15, decimal_places=2)
    f_mes = models.CharField(choices=meses, max_length=2)
    f_año = models.CharField(choices=año, max_length=4)