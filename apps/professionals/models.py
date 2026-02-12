from django.db import models


class Professional(models.Model):
    social_name = models.CharField(max_length=255, verbose_name="Nome Social")
    profession = models.CharField(max_length=100, verbose_name="Profissão")
    address = models.TextField(verbose_name="Endereço")
    contact = models.CharField(max_length=100, verbose_name="Contato")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.social_name} ({self.profession})"

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
        ordering = ["social_name"]
