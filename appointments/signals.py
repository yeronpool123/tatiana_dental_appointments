# appointments/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PatientProfile


# Crear y guardar perfil de paciente automáticamente al crear un usuario
@receiver(post_save, sender=User)
def create_patient_profile(sender, instance, created, **kwargs):
    if created:
        PatientProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_patient_profile(sender, instance, **kwargs):
    # Garantiza que el perfil existe (ej. si viene de Google)
    PatientProfile.objects.get_or_create(user=instance)
    instance.patient_profile.save()
