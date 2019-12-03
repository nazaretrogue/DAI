# práctica_05/urls.py

from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.artistas_list, name='artistas_list'),
    url(r'^artistas/$', views.artistas, name='artistas'),
    url(r'^grupos$', views.grupos, name='grupos'),
    url(r'^albumes/$', views.albumes, name='albumes'),
    url(r'^modificar_artista$', views.modificar_artista, name='modificar_artista'),
    url(r'^borrar_artista$', views.borrar_artista, name='borrar_artista'),
    url(r'^registro$', views.registro, name='registro'),
    url(r'^no_ajax_pag$', views.inicio_pag_no_ajax, name='inicio_pag_no_ajax'),
    url(r'^anterior_pag$', views.anterior_pag, name='anterior_pag'),
    url(r'^siguiente_pag$', views.siguiente_pag, name='siguiente_pag'),
    url(r'^ajax_pag$', views.pag_ajax, name='pag_ajax',)
]
