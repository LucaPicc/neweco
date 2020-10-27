from django import forms
from .models import UserCustom, Entidad

class CrearUserForm(forms.ModelForm):

    password1 = forms.CharField(label = 'Contraseña', max_length=50, widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder':'Introduzca la contraseña',
            'id':'contra1',
            'required':'required',

    }))
    password2 = forms.CharField(label = 'Contraseña verificación', max_length=50, widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder':'Introduzca nuevamente la contraseña',
            'id':'contra1',
            'required':'required',

    }))
    
    class Meta:
        model = UserCustom
        fields = ['username','email','first_name','last_name','entity']
        widgets = {
            'username':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Introduzca un nombre para indentificar al usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Correo eletronico del usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
            'first_name':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'',
                    'id':'username',
                    'required':'required',
                }
            ),
            'last_name':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'',
                    'id':'username',
                    'required':'required',
                }
            ),
            'entity':forms.Select(
                attrs = {
                    'label':'Entidad',
                    'class': 'form-control',
                    'placeholder':'Entidad a la que pertenece el usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
        }
        labels = {
            'username':'Nombre de usuario',
            'email':'Correo electroníco',
            'first_name':'Nombres',
            'last_name':'Apellidos',
            'entity':'Entidad',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

class CrearUserForm2(forms.ModelForm):

    password1 = forms.CharField(label = 'Contraseña', max_length=50, widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder':'Introduzca la contraseña',
            'id':'contra1',
            'required':'required',

    }))
    password2 = forms.CharField(label = 'Contraseña verificación', max_length=50, widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder':'Introduzca nuevamente la contraseña',
            'id':'contra1',
            'required':'required',

    }))
    
    class Meta:
        model = UserCustom
        fields = ['username','email','first_name','last_name']
        widgets = {
            'username':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Introduzca un nombre para indentificar al usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
            'email':forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Correo eletronico del usuario',
                    'id':'username',
                    'required':'required',
                }
            ),
            'first_name':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'',
                    'id':'username',
                    'required':'required',
                }
            ),
            'last_name':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'',
                    'id':'username',
                    'required':'required',
                }
            ),
        }
        labels = {
            'username':'Nombre de usuario',
            'email':'Correo electroníco',
            'first_name':'Nombre',
            'last_name':'Apellido',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

class CrearEntidadForm(forms.ModelForm):
    
    class Meta:
        model = Entidad
        fields = ('nombre','pais','prov','loc','tipo')
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Nombre de la entidad',
                    'id':'nombre-e',
                    'required':'required',
                }
            ),
            'pais': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Pais donde se encuentra radicada la entidad',
                    'id':'pais-e',
                    'required':'required',
                }
            ),
            'prov': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Provincia',
                    'id':'prov-e',
                    'required':'required',
                }
            ),
            'loc':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Localidad',
                    'id':'tipo-e',
                    'required':'required',
                }
            ),
            'tipo': forms.Select(
                attrs = {
                    'class':'form-control',
                    'id':'tipo-e',
                    'required':'required',
                }
            ),
        }
        labels = {
            'nombre':'Nombre',
            'pais':'País',
            'prov':'Provincia',
            'tipo':'Tipo',
        }
