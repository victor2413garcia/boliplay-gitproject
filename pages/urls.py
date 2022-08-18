from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('juegos', views.juegos, name='juegos'),
    path('contacto', views.contacto, name='contacto'),
    path('recarga', views.recarga, name='recarga'),
    path('retiro', views.retiro, name='retiro')
]
