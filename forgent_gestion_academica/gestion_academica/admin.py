from django.contrib import admin
from .models import Relator, Programa, AsignacionRelator, Participante, Inscripcion

@admin.register(Relator)
class RelatorAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "email", "especialidad")
    search_fields = ("nombre_completo", "email", "especialidad")


class AsignacionRelatorInline(admin.TabularInline):
    model = AsignacionRelator
    extra = 1


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo", "tipo", "fecha_inicio", "fecha_fin", "estado", "horas_totales")
    list_filter = ("tipo", "estado")
    search_fields = ("nombre", "codigo")
    inlines = [AsignacionRelatorInline]


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "rut", "email", "servicio", "cargo")
    search_fields = ("nombre_completo", "rut", "email", "servicio")


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("participante", "programa", "estado", "fecha_inscripcion")
    list_filter = ("estado", "programa")
    search_fields = ("participante__nombre_completo", "programa__nombre")