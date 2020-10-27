from django import forms
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


class GsimpleForm(forms.Form):
    reciclables = forms.DecimalField(label= 'Reciclables en Toneladas', required=False, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de toneladas de material recuperado en reciclado',
            'id':'ton_rec',
        }
    ))
    ##Fecha a la que corresponde el registro##
    f_mes = forms.ChoiceField(choices=meses,label='Mes correspondiente a los datos', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    f_año = forms.ChoiceField(choices=año,label='Año correspondiente a los datos', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    ###Empleos##
    em_reco = forms.IntegerField(label='Empleos en recolección',min_value=0, required=False, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en recolección',
            'id':'em_rec'
        }
    ))
    em_clas = forms.IntegerField(label='Empleos en clasificlación', min_value=0,required=False, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en clasificlación',
            'id':'em_clas',
        }
    ))
    em_educ = forms.IntegerField(label='Empleos en educación ambiental',min_value=0, required=False, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en educación ambiental',
            'id':'em_rec'
        }
    ))
    em_disp = forms.IntegerField(label='Empleos en disposición final y tratamiento',min_value=0, required=False, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en disposición final y tratamiento',
            'id':'em_disp',
        }
    ))
    ##Gastos reciclable##
    g_recol = forms.DecimalField(label='Gastos en recolección',min_value=0, required=False,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares de la recolección',
            'id':'g_recol',
        }
    ))
    g_clasf = forms.DecimalField(label='Gastos en clasificación',min_value=0, required=False,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares de la clasificación',
            'id':'g_clasf',
        }
    ))
    g_edu = forms.DecimalField(label='Gastos en educación ambiental',min_value=0, required=False,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares del programa de educación ambiental',
            'id':'g_edu',
        }
    ))
    ##Gastos GIRSU##
    g_disp_trat = forms.DecimalField(label='Gastos en educación ambiental',min_value=0, required=False,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares del programa de educación ambiental',
            'id':'g_edu',
        }
    ))
    
class GIRSUForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all(),label='Entidad', widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    f_mes = forms.ChoiceField(choices=meses,label='Mes correspondiente a los datos', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    f_año = forms.ChoiceField(choices=año,label='Año correspondiente a los datos', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    reciclables = forms.DecimalField(label= 'Reciclables en Toneladas', required=False, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de toneladas de material recuperado en reciclado',
            'id':'ton_rec',
        }
    ))
    ###Empleos##
    em_reco = forms.IntegerField(label='Empleos en recolección', required=False,min_value=0, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en recolección',
            'id':'em_rec'
        }
    ))
    em_clas = forms.IntegerField(label='Empleos en clasificlación', required=False,min_value=0, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en clasificlación',
            'id':'em_clas',
        }
    ))
    em_educ = forms.IntegerField(label='Empleos en educación ambiental', required=False,min_value=0, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en educación ambiental',
            'id':'em_rec'
        }
    ))
    em_disp = forms.IntegerField(label='Empleos en disposición final y tratamiento', required=False,min_value=0, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de personas trabajando en disposición final y tratamiento',
            'id':'em_disp',
        }
    ))
    ##Gastos reciclable##
    g_recol = forms.DecimalField(label='Gastos en recolección', required=False,min_value=0,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares de la recolección',
            'id':'g_recol',
        }
    ))
    g_clasf = forms.DecimalField(label='Gastos en clasificación', required=False,min_value=0,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares de la clasificación',
            'id':'g_clasf',
        }
    ))
    g_edu = forms.DecimalField(label='Gastos en educación ambiental', required=False,min_value=0,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares del programa de educación ambiental',
            'id':'g_edu',
        }
    ))
    ##Gastos GIRSU##
    g_disp_trat = forms.DecimalField(label='Gastos en educación ambiental', required=False,min_value=0,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el gasto en dolares del programa de educación ambiental',
            'id':'g_edu',
        }
    ))

class GrafAñoForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset=Entidad.objects.all(), label='Entidades',widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    año = forms.ChoiceField(choices=año, widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))