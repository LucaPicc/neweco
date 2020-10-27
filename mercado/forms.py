from django import forms
from .models import Mat, Prod


class CargaProdForm(forms.Form):
    nombre = forms.CharField(label='Nombre del producto', max_length=50, required=True, widget= forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nombre del producto',
            'required':'required',
        }
    ))

    descripcion = forms.CharField(label='Descripción breve del producto' ,max_length=250, required=False, widget= forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese una breve descripción del producto',
        }
    ))

    cant_comp = forms.IntegerField(label='Cantidad de componentes del producto',min_value=1, required=True, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad de materiales por los que esta compuesto el producto',
        }
    ))

class CargaMatForm(forms.Form):
    nombre = forms.CharField(label='Nombre del material', max_length=50, required=True, widget= forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nombre del material',
            'required':'required',
        }
    ))

    descripcion = forms.CharField(label='Descripción breve del material' ,max_length=250, required=False, widget= forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese una breve descripción del material',
        }
    ))
    
class ProdMatForm(forms.Form):
    mat = forms.ModelChoiceField(queryset= Mat.objects.all(),label='Material',widget=forms.Select(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el material que compone el producto',
            'required':'required',
        }
    ))
    porc = forms.DecimalField(min_value=0.01 ,max_value=1.00,max_digits=3, decimal_places=2,label='Porcentaje del material',required=True,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el porcentaje del producto compuesto por el material',
        }
    ))

class LocalForm(forms.Form):
    nombre = forms.CharField(label='Localidad',max_length=50, required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el nombre de la localidad',
        }
    ))
    provincia = forms.CharField(label='Provincia',max_length=50, required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el la provincia en la cual se encuentra la localidad',
        }
    ))
    pais = forms.CharField(label='País',max_length=50, required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese el país al que pertenece la localidad',
        }
    ))
    residuos = forms.DecimalField(label='Total de residuos',min_value=0, max_digits=15, decimal_places=2, widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad en toneladas de los residuos solidos recolectados',
        }
    ))
    cant_rec = forms.IntegerField(label='Cantidad de productos reciclables',min_value=1,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese de cuantos productos reciclables se componen los residuos',
        }
    ))   
    porc_rec = forms.DecimalField(label='Porcentaje de reciclado',min_value = 0,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese que porcentaje de la totalidad de los residuos que se tratan se reciclan',
        }
    ))
class CompRecForm(forms.Form):
    prod = forms.ModelChoiceField(queryset= Prod.objects.all(),required=True,label='Producto', widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    porc = forms.DecimalField(min_value=0, max_digits=15, decimal_places=2,label='Proporcion de producto',widget= forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Indique la proporción del producto que compone los residuos',
        }
    ))



