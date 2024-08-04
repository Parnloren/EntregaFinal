from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from appentrega.models import Curso, Profesor, Estudiante, Entregable
from appentrega.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def inicio(request):
    return render(request, 'appentrega/inicio.html')
def cursos(request):
    return render(request, 'appentrega/cursos.html')

def estudiantes(request):
    return render(request, 'appentrega/estudiantes.html')

def profesores(request):
    return render(request, 'appentrega/profesores.html')

def entregables(request):
    return render(request, 'appentrega/entregables.html')

def curso_formulario(request):
    if request.method ==  "POST":

        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], comision=informacion['comision'])
            curso.save()
            return render (request, "appentrega/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request,"appentrega/formcursos.html", {"miFormulario": miFormulario})

def profesor_formulario(request):
    if request.method ==  "POST":

        miFormulario=ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render (request, "appentrega/inicio.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request,"appentrega/formprofesores.html", {"miFormulario": miFormulario})

def estudiante_formulario(request):
    if request.method ==  "POST":

        miFormulario=EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render (request, "appentrega/inicio.html")
    else:
        miFormulario = EstudianteFormulario()
    return render(request,"appentrega/formestudiantes.html", {"miFormulario": miFormulario})
    
def entregable_formulario(request):
    if request.method ==  "POST":

        miFormulario=EntregableFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregable = Entregable (nombre=informacion['nombre'], fecha_de_entrega=informacion['fecha_de_entrega'], entregado=informacion['entregado'])
            entregable.save()
            return render (request, "appentrega/inicio.html")
    else:
        miFormulario = EntregableFormulario()
    return render(request,"appentrega/formentregables.html", {"miFormulario": miFormulario})
    
def busquedaComision(request):

    return render(request, "appentrega/busquedacomision.html")

def buscar(request):
    if request.GET["comision"]:
        # respuesta = f"Estoy buscando la comisión N°: {request.GET['comision'] }"
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "appentrega/resultadosBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos"

    # return HttpResponse(respuesta)
    return render(request, "appentrega/inicio.html", {"cursos":cursos, "comision":comision})


# Esto que está a continuaución es la misma estructura pero con etiquetas completamente distintas porque en un inicio pensé que debía multiplicar esto por cada formulario que creara, me pareció curioso dejarlo asentado como muestra de progreso pero lo arreglé porque sería desprolijo y dificil de leer.
# def curso_formulario(request):
#     if request.method ==  "POST":

#         form_curso=CursoFormulario(request.POST)
#         print(form_curso)
#         if form_curso.is_valid():
#             form_curso_cleaned = form_curso.cleaned_data
#         curso = Curso(nombre=form_curso_cleaned['curso'], comision=form_curso_cleaned['comision'])
#         curso.save()

#         return render (request, "appentrega/base.html")
#     else:
#         mi_formulario = CursoFormulario()
#     return render(request,"appentrega/formcursos.html", {"form_curso": mi_formulario})
