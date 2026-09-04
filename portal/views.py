from django.shortcuts import render
def inicio(request):
    """Vista para la página de inicio"""
    return render(request, 'portal/inicio.html')

def proyectos(request):
    return render(request, 'portal/proyectos.html')

def tipos(request):
    return render(request, 'portal/tipos.html')

def quiensoy(request):
    return render(request, 'portal/quiensoy.html')
# Create your views here.
