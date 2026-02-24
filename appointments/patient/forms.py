from django import forms
from appointments.models import PatientProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['phone', 'birth_date', 'insurance', 'emergency_contact', 'notes']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'insurance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seguro médico'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto de emergencia'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notas adicionales'}),
        }
        labels = {
            'phone': 'Teléfono',
            'birth_date': 'Fecha de nacimiento',
            'insurance': 'Seguro médico',
            'emergency_contact': 'Contacto de emergencia',
            'notes': 'Notas adicionales',
        }
        help_texts = {
            'phone': 'Ingrese su número de teléfono de contacto.',
            'birth_date': 'Seleccione su fecha de nacimiento.',
            'insurance': 'Indique su compañía de seguro médico, si aplica.',
            'emergency_contact': 'Nombre y número de contacto de una persona de emergencia.',
            'notes': 'Cualquier información adicional que sea relevante para su atención médica.',
        }
        error_messages = {
            'phone': {
                'invalid': 'Ingrese un número de teléfono válido.',
            },
            'birth_date': {
                'invalid': 'Ingrese una fecha válida.',
            },
        }
        title = "Editar Perfil"
        description = "Actualice su información personal y de contacto."
        success_message = "¡Perfil actualizado exitosamente!"
        submit_button_text = "Guardar Cambios"
        generic_error_messages = {
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese un valor válido.',
        }
        error_messages = {
            'phone': generic_error_messages,
            'birth_date': generic_error_messages,
            'insurance': generic_error_messages,
            'emergency_contact': generic_error_messages,
            'notes': generic_error_messages,
        }
        verbose_name = "Perfil de Paciente"
        verbose_name_plural = "Perfiles de Pacientes"
