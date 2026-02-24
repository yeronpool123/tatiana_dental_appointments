from django import forms
from .models import ClinicalHistory

class ClinicalHistoryForm(forms.ModelForm):
    class Meta:
        model = ClinicalHistory
        fields = ['medical_background', 'allergies', 'treatments']

        widgets = {
            'medical_background': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe tus antecedentes médicos...'}),
            'allergies': forms.Textarea(attrs={'rows': 3, 'placeholder': '¿Tienes alguna alergia? Si no, deja en blanco...'}),
            'treatments': forms.Textarea(attrs={'rows': 3, 'placeholder': '¿Has recibido algún tratamiento dental previo? Si no, deja en blanco...'}),
        }
        labels = {
            'medical_background': 'Antecedentes Médicos',
            'allergies': 'Alergias',
            'treatments': 'Tratamientos Previos',
        }
        help_texts = {
            'medical_background': 'Incluye cualquier condición médica relevante, como diabetes, hipertensión, etc.',
            'allergies': 'Menciona cualquier alergia que tengas, especialmente a medicamentos o anestésicos.',
            'treatments': 'Describe cualquier tratamiento dental previo que hayas recibido, como extracciones, endodoncias, etc.',
        }
        generic_error_messages = {
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese un valor válido.',
        }
        error_messages = {
            'medical_background': generic_error_messages,
            'allergies': generic_error_messages,
            'treatments': generic_error_messages,
        }
        title = "Formulario de Historia Clínica"
        description = "Complete la siguiente información para crear su historia clínica."
        success_message = "¡Su historia clínica ha sido guardada exitosamente!"
        submit_button_text = "Guardar Historia Clínica"
        


