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
]