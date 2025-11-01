
from django import forms
from .models import Paciente, Medico, Cita

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nombre', 'apellido', 'especialidad', 'numero_licencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-select'}),
            'numero_licencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'medico', 'fecha', 'hora', 'motivo']  # ← Añadido 'hora'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'medico': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),  # Nuevo widget
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].input_formats = [
            '%Y-%m-%d',
            '%d/%m/%Y',
        ]
        self.fields['hora'].input_formats = [
            '%H:%M',
            '%I:%M %p',
        ]