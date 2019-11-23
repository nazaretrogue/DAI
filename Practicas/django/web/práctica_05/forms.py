from django import forms
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
