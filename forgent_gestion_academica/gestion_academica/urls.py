from django.urls import path
from . import views

app_name = "gestion_academica"

urlpatterns = [
    # Página inicial: panel
    path("", views.dashboard, name="dashboard"),

    # Programas académicos (CRUD)
    path("programas/", views.ProgramaListView.as_view(), name="programa_list"),
    path("programas/nuevo/", views.ProgramaCreateView.as_view(), name="programa_create"),
    path("programas/<int:pk>/editar/", views.ProgramaUpdateView.as_view(), name="programa_update"),
    path("programas/<int:pk>/eliminar/", views.ProgramaDeleteView.as_view(), name="programa_delete"),

    # Relatores
    path("relatores/", views.RelatorListView.as_view(), name="relator_list"),
    path("relatores/nuevo/", views.RelatorCreateView.as_view(), name="relator_create"),
    path("relatores/<int:pk>/editar/", views.RelatorUpdateView.as_view(), name="relator_update"),
    path("relatores/<int:pk>/eliminar/", views.RelatorDeleteView.as_view(), name="relator_delete"),

    # Participantes
    path("participantes/", views.ParticipanteListView.as_view(), name="participante_list"),
    path("participantes/nuevo/", views.ParticipanteCreateView.as_view(), name="participante_create"),
    path("participantes/<int:pk>/editar/", views.ParticipanteUpdateView.as_view(), name="participante_update"),
    path("participantes/<int:pk>/eliminar/", views.ParticipanteDeleteView.as_view(), name="participante_delete"),

        # Inscripciones
    path("inscripciones/", views.InscripcionListView.as_view(), name="inscripcion_list"),
    path("inscripciones/nueva/", views.InscripcionCreateView.as_view(), name="inscripcion_create"),
    path("inscripciones/<int:pk>/editar/", views.InscripcionUpdateView.as_view(), name="inscripcion_update"),
    path("inscripciones/<int:pk>/eliminar/", views.InscripcionDeleteView.as_view(), name="inscripcion_delete"),

    # Reportes y estadísticas
    path("reportes/estadisticas/", views.estadisticas, name="estadisticas"),
]
