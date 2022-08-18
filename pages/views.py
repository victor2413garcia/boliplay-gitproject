from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def juegos(request):
    return render(request, 'pages/juegos.html')

def contacto(request):
    return render(request, 'pages/contacto.html')

def recarga(request):
    return render(request, 'pages/recarga.html')

def retiro(request):
    return render(request, 'pages/retiro.html')