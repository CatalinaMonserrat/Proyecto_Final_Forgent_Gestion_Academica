from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import connection
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Programa, Relator, Participante, Inscripcion, AsignacionRelator
from .forms import ProgramaForm, RelatorForm, ParticipanteForm

@login_required
def dashboard(request):
    return render(request, "gestion_academica/dashboard.html")

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

