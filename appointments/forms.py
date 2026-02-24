from django import forms
from .models import Appointment
from datetime import timedelta
from django.utils import timezone



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['cedula','first_name','last_name','phone','description','start']
        widgets = {
            # widget HTML moderno; el formato usa 'YYYY-MM-DDTHH:MM' (datetime-local)
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si se pasa un valor inicial, Django necesita que el campo acepte ese formato
        if 'start' in self.fields:
            self.fields['start'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S']
