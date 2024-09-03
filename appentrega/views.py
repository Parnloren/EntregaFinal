from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregable
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'appentrega/inicio.html')

@login_required
def about(request):
    return render(request, 'appentrega/about.html')


# Cursos Views

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appentrega/listarCurso.html"
    
class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appentrega/createCurso.html"
    success_url = reverse_lazy("ListarCursos")
    fields = ["nombre","comision","profesor", "fecha_inicio", "fecha_fin", "descripcion"]

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appentrega/actualizarCurso.html"
    success_url = reverse_lazy("ListarCursos")
    fields = ["nombre","comision","profesor", "fecha_inicio", "fecha_fin", "descripcion"]

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "appentrega/borrarCurso.html"
    success_url = reverse_lazy("ListarCursos") 

class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "appentrega/detalleCurso.html"

# Profesores Views

class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "appentrega/listarProfesor.html"
    
class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "appentrega/createProfesor.html"
    success_url = reverse_lazy("ListarProfesor")
    fields = ["nombre", "apellido", "email", "profesion"]
    
class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "appentrega/actualizarProfesor.html"
    success_url = reverse_lazy("ListarProfesor")
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    template_name = "appentrega/borrarProfesor.html"
    success_url = reverse_lazy("ListarProfesor") 

class ProfesorDetailView(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = "appentrega/detalleProfesor.html"

# Estudiantes Views
    
class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "appentrega/listarEstudiante.html"
    
class EstudianteCreateView(LoginRequiredMixin, CreateView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "appentrega/createEstudiante.html"
    success_url = reverse_lazy("ListarEstudiante")
    fields = ["nombre", "apellido", "email"]
    
class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "appentrega/actualizarEstudiante.html"
    success_url = reverse_lazy("ListarEstudiante")
    fields = ["nombre", "apellido", "email"]

class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = "appentrega/borrarEstudiante.html"
    success_url = reverse_lazy("ListarEstudiante") 

class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "appentrega/detalleEstudiante.html"

# Entregables Views
    
class EntregableListView(LoginRequiredMixin, ListView):
    model = Entregable
    context_object_name = "entregables"
    template_name = "appentrega/listarEntregable.html"
    
class EntregableCreateView(LoginRequiredMixin, CreateView):
    model = Entregable
    context_object_name = "entregables"
    template_name = "appentrega/createEntregable.html"
    success_url = reverse_lazy("ListarEntregable")
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    
class EntregableUpdateView(LoginRequiredMixin, UpdateView):
    model = Entregable
    context_object_name = "entregables"
    template_name = "appentrega/actualizarEntregable.html"
    success_url = reverse_lazy("ListarEntregable")
    fields = ["nombre", "fecha_de_entrega", "entregado"]

class EntregableDeleteView(LoginRequiredMixin, DeleteView):
    model = Entregable
    template_name = "appentrega/borrarEntregable.html"
    success_url = reverse_lazy("ListarEntregable") 

class EntregableDetailView(LoginRequiredMixin, DetailView):
    model = Entregable
    template_name = "appentrega/detalleEntregable.html"

