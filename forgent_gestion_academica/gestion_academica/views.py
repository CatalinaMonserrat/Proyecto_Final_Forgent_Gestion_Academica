from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import connection
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Programa, Relator, Participante, Inscripcion, AsignacionRelator
from .forms import ProgramaForm, RelatorForm, ParticipanteForm, InscripcionForm

@login_required
def dashboard(request):
    programas_en_ejecucion = Programa.objects.filter(estado="EJECUCION").count()
    total_programas = Programa.objects.count()
    total_relatores = Relator.objects.count()
    total_participantes = Participante.objects.count()
    inscripciones_confirmadas = Inscripcion.objects.filter(estado="CONFIRMADO").count()

    contexto = {
        "programas_en_ejecucion": programas_en_ejecucion,
        "total_programas": total_programas,
        "total_relatoreS": total_relatores,
        "total_participantes": total_participantes,
        "inscripciones_confirmadas": inscripciones_confirmadas,
    }
    return render(request, "gestion_academica/dashboard.html", contexto)

def custom_logout(request):
    """
    Cierra la sesión del usuario y redirige al login.
    Permite llamadas GET sin error 405.
    """
    logout(request)
    return redirect("login")

@method_decorator(login_required, name="dispatch")
class ProgramaListView(ListView):
    model = Programa
    template_name = "gestion_academica/programa_list.html"
    context_object_name = "programas"


@method_decorator(login_required, name="dispatch")
class ProgramaCreateView(CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = "gestion_academica/programa_form.html"
    success_url = reverse_lazy("gestion_academica:programa_list")


@method_decorator(login_required, name="dispatch")
class ProgramaUpdateView(UpdateView):
    model = Programa
    form_class = ProgramaForm
    template_name = "gestion_academica/programa_form.html"
    success_url = reverse_lazy("gestion_academica:programa_list")


@method_decorator(login_required, name="dispatch")
class ProgramaDeleteView(DeleteView):
    model = Programa
    template_name = "gestion_academica/programa_confirm_delete.html"
    success_url = reverse_lazy("gestion_academica:programa_list")

@method_decorator(login_required, name="dispatch")
class RelatorListView(ListView):
    model = Relator
    template_name = "gestion_academica/relator_list.html"
    context_object_name = "relatores"


@method_decorator(login_required, name="dispatch")
class RelatorCreateView(CreateView):
    model = Relator
    form_class = RelatorForm
    template_name = "gestion_academica/relator_form.html"
    success_url = reverse_lazy("gestion_academica:relator_list")


@method_decorator(login_required, name="dispatch")
class RelatorUpdateView(UpdateView):
    model = Relator
    form_class = RelatorForm
    template_name = "gestion_academica/relator_form.html"
    success_url = reverse_lazy("gestion_academica:relator_list")


@method_decorator(login_required, name="dispatch")
class RelatorDeleteView(DeleteView):
    model = Relator
    template_name = "gestion_academica/relator_confirm_delete.html"
    success_url = reverse_lazy("gestion_academica:relator_list")

@method_decorator(login_required, name="dispatch")
class ParticipanteListView(ListView):
    model = Participante
    template_name = "gestion_academica/participante_list.html"
    context_object_name = "participantes"


@method_decorator(login_required, name="dispatch")
class ParticipanteCreateView(CreateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = "gestion_academica/participante_form.html"
    success_url = reverse_lazy("gestion_academica:participante_list")


@method_decorator(login_required, name="dispatch")
class ParticipanteUpdateView(UpdateView):
    model = Participante
    form_class = ParticipanteForm
    template_name = "gestion_academica/participante_form.html"
    success_url = reverse_lazy("gestion_academica:participante_list")


@method_decorator(login_required, name="dispatch")
class ParticipanteDeleteView(DeleteView):
    model = Participante
    template_name = "gestion_academica/participante_confirm_delete.html"
    success_url = reverse_lazy("gestion_academica:participante_list")

@login_required
def estadisticas(request):
    # Cursos con más inscritos
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.nombre, COUNT(i.id) AS total_inscritos
            FROM gestion_academica_programa p
            LEFT JOIN gestion_academica_inscripcion i
                ON p.id = i.programa_id
            GROUP BY p.id, p.nombre
            ORDER BY total_inscritos DESC
            LIMIT 5;
        """)
        top_cursos = cursor.fetchall()  # [(nombre, total), ...]

    # Relatores con más horas asignadas
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.nombre_completo, SUM(ar.horas_asignadas) AS horas_totales
            FROM gestion_academica_relator r
            JOIN gestion_academica_asignacionrelator ar
                ON r.id = ar.relator_id
            GROUP BY r.id, r.nombre_completo
            ORDER BY horas_totales DESC;
        """)
        top_relatores = cursor.fetchall()  # [(nombre, horas), ...]

    contexto = {
        "top_cursos": top_cursos,
        "top_relatores": top_relatores,
    }
    return render(request, "gestion_academica/estadisticas.html", contexto)

@method_decorator(login_required, name="dispatch")
class InscripcionListView(ListView):
    model = Inscripcion
    template_name = "gestion_academica/inscripcion_list.html"
    context_object_name = "inscripciones"


@method_decorator(login_required, name="dispatch")
class InscripcionCreateView(CreateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "gestion_academica/inscripcion_form.html"
    success_url = reverse_lazy("gestion_academica:inscripcion_list")


@method_decorator(login_required, name="dispatch")
class InscripcionUpdateView(UpdateView):
    model = Inscripcion
    form_class = InscripcionForm
    template_name = "gestion_academica/inscripcion_form.html"
    success_url = reverse_lazy("gestion_academica:inscripcion_list")


@method_decorator(login_required, name="dispatch")
class InscripcionDeleteView(DeleteView):
    model = Inscripcion
    template_name = "gestion_academica/inscripcion_confirm_delete.html"
    success_url = reverse_lazy("gestion_academica:inscripcion_list")