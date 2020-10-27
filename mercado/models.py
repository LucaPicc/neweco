from django.db import models

# Create your models here.
class Localidad(models.Model):
    nom = models.CharField( max_length=50)
    pais = models.CharField( max_length=50)
    prov = models.CharField( max_length=50)
    pob = models.IntegerField()
    g_rec_sol = models.DecimalField( max_digits=15, decimal_places=2)
    g_rec_sol_rec = models.DecimalField( max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nom
    

class Prod(models.Model):
    nom = models.CharField( max_length=50,unique=True)
    descr = models.CharField( max_length=250)

    def __str__(self):
        return self.nom
    

class Mat(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    desc = models.CharField( max_length=250)

    def __str__(self):
        return self.nom
    

class ProdMat(models.Model):
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    mat = models.ForeignKey(Mat, on_delete=models.CASCADE)
    porc = models.DecimalField( max_digits=4, decimal_places=2)

    def __str__(self):
        return self.prod
    

class CompRec(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    prod = models.ForeignKey(Prod, on_delete=models.CASCADE)
    porc = models.DecimalField( max_digits=4, decimal_places=2)

    def __str__(self):
        return self.localidad
    

