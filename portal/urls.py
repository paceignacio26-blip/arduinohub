from django.urls import path
from . import views
urlpatterns = [
path('', views.inicio, name='inicio'),
path('proyectos/', views.proyectos, name='proyectos'),
path('tipos/', views.tipos, name='tipos'),
path('quiensoy/', views.quiensoy, name='quiensoy'),

]