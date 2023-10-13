from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppLogin.models import Avatar

class RegistroUsuario(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model= User
        fields = ["username","email","first_name","password1","password2"]

class EditarUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre')                            

    class Meta:
        model= User
        fields = ["email","first_name","password1","password2"]

class Avatar_Form (forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]