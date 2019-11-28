from django import forms
from django.contrib.auth.models import User
from .models import Musico, Album, GrupoMusical

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ('nombre', 'apellidos', 'fnac', 'instrumento',)

class GrupoMusicalForm(forms.ModelForm):
    class Meta:
        model = GrupoMusical
        fields = ('nombre', 'creacion', 'estilo', 'miembros',)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artista', 'nombre', 'lanzamiento', 'estrellas',)

class RegistroForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget = forms.PasswordInput)
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)

class LoginForm(forms.Form):
        username = forms.CharField(max_length=150)
        password = forms.CharField(widget = forms.PasswordInput)

# class LoginForm(forms.ModelForm):
#     class Meta:
#         password = forms.CharField(widget = forms.PasswordInput)
#         model = User
#         widgets = {
#             'password': forms.PasswordInput(),
#         }
#         fields = ('username', 'password',)
