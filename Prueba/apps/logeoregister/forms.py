from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields

def AgregarFormControl(campos):
    for camposVisibles in campos:
        camposVisibles.field.widget.attrs['class'] = 'form control'


class RegistroUsuario(UserCreationForm):
        
    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        AgregarFormControl(self.visible_fields())

    class Meta: 
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')


class IniciarSesion(AuthenticationForm): 
    def __init__(self, request, *args, **kwargs): 
        super().__init__(request=request, *args, **kwargs)
        AgregarFormControl(self.visible_fields())


    class Meta:
        fields = ('username','password')