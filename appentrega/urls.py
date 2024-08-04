from django.urls import path
from appentrega.views import inicio, cursos, estudiantes, profesores, entregables, curso_formulario, profesor_formulario, estudiante_formulario, entregable_formulario, busquedaComision, buscar
urlpatterns = [
    path('cursoss/', cursos, name='cursos'),
    path('', inicio, name='inicio'),
    path('estudiantess/', estudiantes, name='estudiantes'),
    path('profesoress/', profesores, name='profesores'),
    path('entregabless/', entregables, name='entregables'),
    path('busquedaComision', busquedaComision, name="BusquedaComision"),
    path('buscar/', buscar),
]
urlformularios = [
    path('cursos/', curso_formulario, name="CursoFormulario" ),
    path('profesores/', profesor_formulario, name="ProfesorFormulario" ),
    path('estudiantes/', estudiante_formulario, name="EstudianteFormulario" ),
    path('entregables/', entregable_formulario, name="EntregableFormulario" ),
]
# urlbusquedas = [

# ]
urlpatterns += urlformularios
# urlpatterns += urlbusquedas