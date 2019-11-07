from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def test_template(request):
    context = {}
    return render(request, 'test.html', context)
