from django.contrib import admin
from .models import Musico, GrupoMusical, Album

# Register your models here.

admin.site.register(Musico)
admin.site.register(Album)
admin.site.register(GrupoMusical)
