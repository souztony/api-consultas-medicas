from django.db import models
from apps.professionals.models import Professional


class Appointment(models.Model):
    date = models.DateTimeField(verbose_name="Data da Consulta")
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name="Profissional",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consulta com {self.professional.social_name} em {self.date}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ["-date"]
