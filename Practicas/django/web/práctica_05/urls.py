# práctica_05/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.artistas_list, name='artistas_list'),
    url(r'^test_template/$', views.test_template, name='test_template'),
    url(r'^artistas/$', views.artistas, name='artistas'),
    url(r'^grupos/$', views.grupos, name='grupos'),
    url(r'^albumes/$', views.albumes, name='albumes'),
]
