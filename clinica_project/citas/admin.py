from django.contrib import admin
from .models import Medico, Especialidad  # Asegúrate de importar ambos modelos

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_especialidad',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'especialidad')