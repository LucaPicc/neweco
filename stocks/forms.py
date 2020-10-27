from django import forms
from .models import StockProd
from mercado.models import Prod,Mat
from user.models import Entidad


class IngStockProdForm(forms.Form):
    prod = forms.ModelChoiceField(queryset=Prod.objects.all(),label='Producto',widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    unidad = forms.ChoiceField(label='Unidad de medida',choices=[('Kg','KiloGramos'),('Tn','Toneladas')],required=True,widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    cantidad = forms.DecimalField(label='Cantidad en la unidad guardada',required=True, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
        }
    ))

class IngStockMatForm(forms.Form):
    mat = forms.ModelChoiceField(queryset=Mat.objects.all(),label='Material',widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    unidad = forms.ChoiceField(label='Unidad de medida',choices=[('Kg','KiloGramos'),('Tn','Toneladas')],required=True,widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    cantidad = forms.DecimalField(label='Cantidad en la unidad guardada',required=True, widget=forms.NumberInput(
        attrs={
            'class':'form-control',
        }
    ))

class EnvPForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset= Entidad.objects.all(),label='Entidad receptora',widget= forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    producto = forms.ModelChoiceField(queryset= Prod.objects.all(),widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    unidad = forms.ChoiceField(label='Unidad de medida',choices=[('Kg','KiloGramos'),('Tn','Toneladas')],widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    cantidad = forms.DecimalField(label='Cantidad a enviar',min_value=0.01,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad a enviar considerando la unidad seleccionada',
        }
    ))
class EnvMForm(forms.Form):
    entidad = forms.ModelChoiceField(queryset= Entidad.objects.all(),label='Entidad receptora',widget= forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    material = forms.ModelChoiceField(queryset= Mat.objects.all(),widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    unidad = forms.ChoiceField(label='Unidad de medida',choices=[('Kg','KiloGramos'),('Tn','Toneladas')],widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))
    cantidad = forms.DecimalField(label='Cantidad a enviar',min_value=0.01,widget=forms.NumberInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la cantidad a enviar considerando la unidad seleccionada',
        }
    ))
