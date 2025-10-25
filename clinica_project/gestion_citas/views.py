# app_citas/views.py
from django.shortcuts import render

def paciente_list(request):
    return render(request, 'gestion_citas/paciente_list.html', {
        'title': 'Sistema de Citas Médicas'
    })