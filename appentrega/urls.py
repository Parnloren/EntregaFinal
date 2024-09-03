from django.urls import path
from appentrega.views import inicio, about
from appentrega import views
urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='About'),
    
    #Cursos

    path("listar_curso/", views.CursoListView.as_view(), name= "ListarCursos"),
    path("crear_curso/", views.CursoCreateView.as_view(), name= "CrearCurso"),
    path("actualizar_curso/<pk>", views.CursoUpdateView.as_view(), name= "ActualizarCurso"),
    path("borrar_curso/<pk>", views.CursoDeleteView.as_view(), name= "BorrarCurso"),
    path("detalle_curso/<pk>", views.CursoDetailView.as_view(), name= "DetalleCurso"),

    #Profesores

    path("listar_profesor/", views.ProfesorListView.as_view(), name= "ListarProfesor"),
    path("crear_profesor/", views.ProfesorCreateView.as_view(), name= "CrearProfesor"),
    path("actualizar_profesor/<pk>", views.ProfesorUpdateView.as_view(), name= "ActualizarProfesor"),
    path("borrar_profesor/<pk>", views.ProfesorDeleteView.as_view(), name= "BorrarProfesor"),
    path("detalle_profesor/<pk>", views.ProfesorDetailView.as_view(), name= "DetalleProfesor"),

    #Estudiantes

    path("listar_estudiante/", views.EstudianteListView.as_view(), name= "ListarEstudiante"),
    path("crear_estudiante/", views.EstudianteCreateView.as_view(), name= "CrearEstudiante"),
    path("actualizar_estudiante/<pk>", views.EstudianteUpdateView.as_view(), name= "ActualizarEstudiante"),
    path("borrar_estudiante/<pk>", views.EstudianteDeleteView.as_view(), name= "BorrarEstudiante"),
    path("detalle_estudiante/<pk>", views.EstudianteDetailView.as_view(), name= "DetalleEstudiante"),

    #Entregables

    path("listar_entregable/", views.EntregableListView.as_view(), name= "ListarEntregable"),
    path("crear_entregable/", views.EntregableCreateView.as_view(), name= "CrearEntregable"),
    path("actualizar_entregable/<pk>", views.EntregableUpdateView.as_view(), name= "ActualizarEntregable"),
    path("borrar_entregable/<pk>", views.EntregableDeleteView.as_view(), name= "BorrarEntregable"),
    path("detalle_entregable/<pk>", views.EntregableDetailView.as_view(), name= "DetalleEntregable"),
]
# urlformularios = [
#     path('cursos/', curso_formulario, name="CursoFormulario" ),
#     path('                                                                                                                    es/', profesor_formulario, name="ProfesorFormulario" ),
#     path('estudiantes/', estudiante_formulario, name="EstudianteFormulario" ),
#     path('entregables/', entregable_formulario, name="EntregableFormulario" ),
# ]
# urlbusquedas = [

# ]
# urlpatterns += urlformularios
# urlpatterns += urlbusquedas