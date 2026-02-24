# appointments/apps.py
from django.apps import AppConfig

# Configuración de la app de citas
class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments'

    def ready(self):
        from . import signals  # noqa
        # Importa los signals para que se registren
