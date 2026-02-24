from django.db import models
from django.contrib.auth.models import User

class ClinicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    medical_background = models.TextField(verbose_name="Antecedentes médicos")
    allergies = models.TextField(blank=True, null=True, verbose_name="Alergias")
    treatments = models.TextField(blank=True, null=True, verbose_name="Tratamientos previos")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historia clínica de {self.patient.username}"

