# citas/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm

# === PACIENTE ===
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'citas/paciente_list.html', {'pacientes': pacientes})

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nuevo Paciente'})

def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'citas/form.html', {'form': form, 'title': 'Editar Paciente'})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'citas/confirm_delete.html', {'obj': paciente, 'type': 'Paciente'})

# === MEDICO ===
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'citas/medico_list.html', {'medicos': medicos})

def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nuevo Médico'})

def medico_update(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'citas/form.html', {'form': form, 'title': 'Editar Médico'})

def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'citas/confirm_delete.html', {'obj': medico, 'type': 'Médico'})

# === CITA ===
def cita_list(request):
    citas = Cita.objects.select_related('paciente', 'medico').all()
    return render(request, 'citas/cita_list.html', {'citas': citas})

def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nueva Cita'})

def cita_update(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'citas/form.html', {'form': form, 'title': 'Editar Cita'})

def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('cita_list')
    return render(request, 'citas/confirm_delete.html', {'obj': cita, 'type': 'Cita'})

from django.shortcuts import render, get_object_or_404
from .models import Paciente, Medico, Cita

def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'citas/paciente_detail.html', {'paciente': paciente})

def medico_detail(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    return render(request, 'citas/medico_detail.html', {'medico': medico})

def cita_detail(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'citas/cita_detail.html', {'cita': cita})

# citas/views.py
from django.shortcuts import redirect

def home(request):
    return redirect('paciente_list')

# citas/views.py
from django.shortcuts import render

def paciente_list(request):
    return render(request, 'citas/paciente_list.html', {
        'title': 'Lista de Pacientes'
    })