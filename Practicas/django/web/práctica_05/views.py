from django.shortcuts import render, HttpResponse
from django.forms.models import model_to_dict
from .models import Musico
from .forms import MusicoForm, GrupoMusicalForm, AlbumForm

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def test_template(request):
    context = {}
    return render(request, 'test.html', context)

def artistas(request):
    if request.method == 'POST':
        form = MusicoForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = MusicoForm()

    return render(request, 'artistas.html', {'form': form})

def grupos(request):
    if request.method == 'POST':
        form = GrupoMusicalForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = GrupoMusicalForm()

    return render(request, 'grupos.html', {'form': form})

def albumes(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = AlbumForm()

    return render(request, 'albumes.html', {'form': form})
