from django.shortcuts import render, redirect
from .models import Inscrito, Institucion
from .forms import InscritoForm, InstitucionForm

def index(request):
    return render(request, 'index.html')

#Metodos CRUD para Inscritos 

def lista_inscritos(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'lista_inscritos.html', {'inscritos': inscritos})

def agregar_inscrito(request):
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscritos')
    else:
        form = InscritoForm()
    return render(request, 'agregar_inscrito.html', {'form': form})

def editar_inscrito(request, id):
    inscrito = Inscrito.objects.get(id=id)
    if request.method == 'GET':
        form = InscritoForm(instance=inscrito)
    else:
        form = InscritoForm(request.POST, instance=inscrito)
        if form.is_valid():
            form.save()
            return redirect('lista_inscritos')
    return render(request, 'agregar_inscrito.html', {'form': form})

def eliminar_inscrito(request, id):
    if request.method == 'POST':
        inscrito = Inscrito.objects.get(id=id)
        inscrito.delete()
        return redirect('lista_inscritos')
    
    else:
        return redirect('lista_inscritos')
    

#Metodos CRUD para Instituciones

def lista_instituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'lista_instituciones.html', {'instituciones': instituciones})

def agregar_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_instituciones')
    else:
        form = InstitucionForm()
    return render(request, 'agregar_institucion.html', {'form': form})

def editar_institucion(request, id):
    institucion = Institucion.objects.get(id=id)
    if request.method == 'GET':
        form = InstitucionForm(instance=institucion)
    else:
        form = InstitucionForm(request.POST, instance=institucion)
        if form.is_valid():
            form.save()
            return redirect('lista_instituciones')
    return render(request, 'agregar_institucion.html', {'form': form})

def eliminar_institucion(request, id):
    if request.method == 'POST':
        institucion = Institucion.objects.get(id=id)
        institucion.delete()
        return redirect('lista_instituciones')
    
    else:
        return redirect('lista_instituciones')
