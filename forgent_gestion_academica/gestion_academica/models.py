from django.db import models


class Relator(models.Model):
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_completo


class Programa(models.Model):
    TIPO_CHOICES = [
        ("CURSO", "Curso"),
        ("DIPLOMADO", "Diplomado"),
    ]

    ESTADO_CHOICES = [
        ("PLANIFICADO", "Planificado"),
        ("EJECUCION", "En ejecución"),
        ("FINALIZADO", "Finalizado"),
    ]

    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    horas_totales = models.PositiveIntegerField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="PLANIFICADO"
    )

    # Relación M2M con Relator usando tabla intermedia
    relatores = models.ManyToManyField(
        "Relator",
        through="AsignacionRelator",
        related_name="programas"
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class AsignacionRelator(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    relator = models.ForeignKey(Relator, on_delete=models.CASCADE)
    horas_asignadas = models.PositiveIntegerField()

    class Meta:
        unique_together = ("programa", "relator")

    def __str__(self):
        return f"{self.relator} en {self.programa} - {self.horas_asignadas} hrs"


class Participante(models.Model):
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField()
    rut = models.CharField(max_length=20)
    servicio = models.CharField(max_length=200, blank=True, null=True)
    cargo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.rut}"


class Inscripcion(models.Model):
    ESTADO_CHOICES = [
        ("PREINSCRITO", "Preinscrito"),
        ("CONFIRMADO", "Confirmado"),
        ("RECHAZADO", "Rechazado"),
    ]

    participante = models.ForeignKey(
        Participante,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default="PREINSCRITO"
    )

    class Meta:
        unique_together = ("participante", "programa")

    def __str__(self):
        return f"{self.participante} en {self.programa} ({self.estado})"