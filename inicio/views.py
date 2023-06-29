from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from inicio.models import Perro
from django.shortcuts import render, redirect
from inicio.form import CrearPerroFormulario, BuscarPerroFormulario

#v1
# def inicio(request):
#     return HttpResponse('Hola Hola Hola')

#v2
# def inicio(request):
#     archivo = open(r'C:\Users\florv\Documents\CODERHOUSE\PYTHON\CLASES\proyectoFinalPython\proyectoFinalPython\templates\inicio.html', 'r')
#     template = Template(archivo.read())
#     archivo.close()
#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25)),
#     }
#     contexto = Context(diccionario)
#     renderizar_template = template.render(contexto)
#     return HttpResponse(renderizar_template)

#v3
# def inicio(request):
#     template = loader.get_template('inicio.html')

#     segundos = datetime.now().second
#     diccionario = {
#         'mensaje': 'Este es el mensaje de inicio...',
#         'segundos': segundos,
#         'segundo_par': segundos%2 == 0,
#         'segundo_redondo': segundos%10 == 0,
#         'listado_de_numeros': list(range(25)),
#     }

#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

#v4
def inicio(request):
    return render(request, 'inicio/inicio.html')

def prueba(request):
    segundos = datetime.now().second
    diccionario = {
        'mensaje': 'Este es el mensaje de inicio...',
        'segundos': segundos,
        'segundo_par': segundos%2 == 0,
        'segundo_redondo': segundos%10 == 0,
        'listado_de_numeros': list(range(25)),
    }

    return render(request, 'inicio/prueba.html', diccionario)


def segunda_vista(request):
    return HttpResponse('<h1>Soy la segunda vista</h1>')

#v1
# def crear_perro(request, nombre, edad):
#     template = loader.get_template('crear_perro.html')
    
#     #V1
#     # diccionario = {
#     #     'nombre': nombre,
#     #     'edad': edad
#     # }

#     #V2
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro
#     }

#     renderizar_template = template.render(diccionario)
#     return HttpResponse(renderizar_template)

#v2
# def crear_perro(request, nombre, edad):
#     perro = Perro(nombre=nombre, edad=edad)
#     perro.save()
#     diccionario = {
#         'perro': perro
#     }
#     return render(request, 'inicio/crear_perro.html', diccionario)

#v3
# def crear_perro(request):
#     diccionario = {}

#     if request.method == 'POST':
#         perro = Perro(nombre=request.POST['nombre'], edad=request.POST['edad'])
#         perro.save()
#         diccionario['perro'] = perro

#     return render(request, 'inicio/crear_perro.html', diccionario)

#v4
# def crear_perro(request):
#     diccionario = {}

#     if request.method == 'POST':
#         formulario = CrearPerroFormulario(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             perro = Perro(nombre=info['nombre'], edad=info['edad'])
#             perro.save()
#             diccionario['perro'] = perro
#             return render(request, 'inicio/perro.html', diccionario)
#         else:
#             diccionario['formulario'] = formulario
#             return render(request, 'inicio/crear_perro.html', diccionario)

#     formulario = CrearPerroFormulario()
#     diccionario['formulario'] = formulario
#     return render(request, 'inicio/crear_perro.html', diccionario)

# v5
def crear_perro(request):

    if request.method == 'POST':
        formulario = CrearPerroFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro = Perro(nombre=info['nombre'], edad=info['edad'])
            perro.save()
            return redirect('inicio:listar_perros')
        else:
            return render(request, 'inicio/crear_perros.html', {'formulario': formulario})

    formulario = CrearPerroFormulario()
    return render(request, 'inicio/crear_perros.html', {'formulario': formulario})

def listar_perros(request):
    formulario = BuscarPerroFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
    listado_de_perros = Perro.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = BuscarPerroFormulario()
    return render(request, 'inicio/listar_perros.html', {'formulario': formulario, 'perros': listado_de_perros, 'busqueda': nombre_a_buscar})