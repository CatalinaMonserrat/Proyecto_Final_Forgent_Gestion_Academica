from django import forms
from .models import Programa, Relator, Participante, Inscripcion


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            "nombre",
            "codigo",
            "tipo",
            "descripcion",
            "fecha_inicio",
            "fecha_fin",
            "horas_totales",
            "estado"
        ]
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            "nombre",
            "codigo",
            "tipo",
            "descripcion",
            "fecha_inicio",
            "fecha_fin",
            "horas_totales",
            "estado"
        ]
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }


class RelatorForm(forms.ModelForm):
    class Meta:
        model = Relator
        fields = [
            "nombre_completo",
            "email",
            "telefono",
            "especialidad",
            "bio",
        ]

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = [
            "nombre_completo",
            "rut",
            "email",
            "servicio",
            "cargo",
        ]

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = [
            "participante",
            "programa",
            "estado",
        ]