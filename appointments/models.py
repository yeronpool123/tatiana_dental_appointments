from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

# appointments/models.py (añade esto arriba, junto con los imports)

from datetime import datetime, time, timedelta


# Horario de atención (ajústalo si quieres)
WORKDAY_START = time(8, 0)   # 08:00
WORKDAY_END   = time(17, 0)  # 17:00

def generate_time_slots_for_date(selected_date, slot_minutes=30):
    """
    Devuelve una lista de datetimes (inicio del slot) para la fecha seleccionada.
    Ejemplo: [datetime(2025,12,03,8,0), datetime(2025,12,03,8,30), ...]
    """
    slots = []
    start_dt = datetime.combine(selected_date, WORKDAY_START)
    end_dt = datetime.combine(selected_date, WORKDAY_END)

    while start_dt + timedelta(minutes=slot_minutes) <= end_dt:
        slots.append(start_dt)
        start_dt += timedelta(minutes=slot_minutes)

    return slots


# Modelo de Cita
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    cedula = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(editable=False)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pendiente"),
            ("confirmed", "Confirmada"),
            ("cancelled", "Cancelada")
        ],
        default="pending"
    )


    def clean(self):
        """
        Validación anti-choque:
        - Asegura end > start
        - Revisa que no existan citas que se solapen: start < other.end AND end > other.start
        """
        # Calcular end previsto (si no lo han puesto)
        if not self.end:
            proposed_end = self.start + timedelta(minutes=30)
        else:
            proposed_end = self.end

        if proposed_end <= self.start:
            raise ValidationError("La hora de fin debe ser mayor que la de inicio.")

        # Buscar solapamientos
        overlaps = Appointment.objects.filter(start__lt=proposed_end, end__gt=self.start)
        if self.pk:
            overlaps = overlaps.exclude(pk=self.pk)

        if overlaps.exists():
            raise ValidationError("El horario seleccionado ya está ocupado. Elige otro.")

    def save(self, *args, **kwargs):
        # Si no se definió end, lo calculamos (duración fija 30 min)
        if not self.end:
            self.end = self.start + timedelta(minutes=30)
        # Forzar validación antes de guardar (esto lanza ValidationError si falla)
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.start.isoformat()}"




# Modelo de Perfil de Paciente
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    insurance = models.CharField(max_length=120, blank=True)
    emergency_contact = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Paciente: {self.user.get_full_name() or self.user.username}"





