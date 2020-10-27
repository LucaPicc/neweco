from django import forms
from user.models import Entidad


class ContactForm(forms.Form):
    email_contac = forms.EmailField(label = 'Su Correo de contacto',widget = forms.EmailInput(attrs = {
        'class' : 'form-control',
        'label' : 'Su correo de contacto',
        'id' : 'email-contacto',
        'required':'required',
    }))

    asunto  = forms.CharField(label = 'Asunto', max_length=250, widget = forms.TextInput(attrs = {
        'class' : 'form-control',
        'label' : 'Su correo de contacto',
        'id' : 'email-contacto',
        'required':'required',
    }))


    cuerpo  = forms.CharField(label='Mensaje', max_length=250, widget = forms.Textarea(attrs = {
        'class' : 'form-control',
        'label' : 'Su correo de contacto',
        'id' : 'email-contacto',
        'required':'required',
    }))


    
