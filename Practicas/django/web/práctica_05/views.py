from django.shortcuts import render, HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Musico, GrupoMusical, Album
from .forms import MusicoForm, GrupoMusicalForm, AlbumForm, RegistroForm, LoginForm
import json

# Create your views here.

user_activo = ""
index_pag_no_ajax = 0

def index(request):
    return HttpResponse('Hello world')

def artistas_list(request):
    artistas = Musico.objects.all()

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'artistas_list.html', {'login': user_activo, 'artistas': artistas})

    else:
        return render(request, 'artistas_list.html', {'artistas': artistas})

@login_required
def artistas(request):
    user_activo = request.user.username
    if request.method == 'POST':
        form = MusicoForm(request.POST)

        if form.is_valid():
            form.save()
            artistas = Musico.objects.all()
            return render(request, 'artistas_list.html', {'artistas': artistas, 'login': user_activo})

    else:
        form = MusicoForm()

    return render(request, 'artistas.html', {'form': form, 'login': user_activo})

@login_required
def grupos(request):
    user_activo = request.user.username
    if request.method == 'POST':
        form = GrupoMusicalForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = GrupoMusicalForm()

    return render(request, 'grupos.html', {'form': form, 'login': user_activo})

@login_required
def albumes(request):
    user_activo = request.user.username
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = AlbumForm()

    return render(request, 'albumes.html', {'form': form, 'login': user_activo})

@login_required
def modificar_artista(request):
    user_activo = request.user.username
    if request.method == 'POST' and 'modificado' in request.POST:
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        fnac = request.POST.get('fnac')
        instrumento = request.POST.get('instrumento')
        Musico.objects.filter(nombre=nombre).update(nombre=nombre, apellidos=apellidos,
                              fnac=fnac, instrumento=instrumento)

        artistas = Musico.objects.all()
        return render(request, 'artistas_list.html', {'artistas': artistas, 'login': user_activo})

    else:
        pk = request.POST.get('pk_artista')
        artista = Musico.objects.get(pk=pk)
        data = {'nombre': artista.nombre, 'apellidos': artista.apellidos, 'fnac': artista.fnac, 'instrumento': artista.instrumento}
        form = MusicoForm(data)
        return render(request, 'modificar_artista.html', {'form': form, 'login': user_activo})

@login_required
def borrar_artista(request):
    user_activo = request.user.username
    Musico.objects.filter(pk=request.POST.get('pk_artista')).delete()
    artistas = Musico.objects.all()
    return render(request, 'artistas_list.html', {'artistas': artistas, 'login': user_activo})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            #form.save()
            artistas = Musico.objects.all()
            return render(request, 'artistas_list.html', {'artistas': artistas})

    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

@login_required
def deslogueo(request):
    logout(request)
    user_activo = ""

    artistas = Musico.objects.all()
    return render(request, 'artistas_list.html', {'artistas': artistas})

def inicio_pag_no_ajax(request):
    global index_pag_no_ajax
    index_pag_no_ajax = 0
    listado = GrupoMusical.objects.all()[index_pag_no_ajax:index_pag_no_ajax+5]

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'paginador_no_ajax.html', {'listado': listado, 'login': user_activo})

    else:
        return render(request, 'paginador_no_ajax.html', {'listado': listado})

def anterior_pag(request):
    global index_pag_no_ajax

    if index_pag_no_ajax <= 5:
        index_pag_no_ajax = 0

    else:
        index_pag_no_ajax -= 5

    listado = GrupoMusical.objects.all()[index_pag_no_ajax:index_pag_no_ajax+5]

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'paginador_no_ajax.html', {'listado': listado, 'login': user_activo})

    else:
        return render(request, 'paginador_no_ajax.html', {'listado': listado})

def siguiente_pag(request):
    global index_pag_no_ajax
    index_pag_no_ajax += 5
    listado = GrupoMusical.objects.all()[index_pag_no_ajax:index_pag_no_ajax+5]

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'paginador_no_ajax.html', {'listado': listado, 'login': user_activo})

    else:
        return render(request, 'paginador_no_ajax.html', {'listado': listado})

def pag_ajax(request):
    listado_total = GrupoMusical.objects.all()
    paginator = Paginator(listado_total, 5)

    page = request.GET.get('page')
    listado = paginator.get_page(page)

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'paginador_ajax.html', {'listado': listado, 'login': user_activo})

    else:
        return render(request, 'paginador_ajax.html', {'listado': listado})

def mapa(request):
    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'mapa.html', {'login': user_activo})

    else:
        return render(request, 'mapa.html')

def charts(request):
    lista_albumes = {}
    set_artistas = set()
    albumes = Album.objects.all()

    for album in albumes:
        lista_albumes[album.artista.nombre] = 0

    for album in albumes:
        set_artistas.add(album.artista.nombre)
        lista_albumes[album.artista.nombre] += 1

    lista_artistas = list(set_artistas)
    # lista_artistas = [(k, v) for k, v in dict_artistas.items()]

    if request.user.is_authenticated:
        user_activo = request.user.username
        return render(request, 'charts.html', {'login': user_activo, 'num_albumes_artista': json.dumps(lista_albumes), 'artistas': json.dumps(lista_artistas)})

    else:
        return render(request, 'charts.html', {'num_albumes_artista': json.dumps(lista_albumes), 'artistas': json.dumps(lista_artistas)})
