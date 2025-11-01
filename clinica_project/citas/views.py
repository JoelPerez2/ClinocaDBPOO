# citas/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Medico, Cita
from .forms import PacienteForm, MedicoForm, CitaForm
from django.contrib.auth.decorators import login_required


# === VISTA DE INICIO ===
def home(request):
    return render(request, 'citas/home.html')


# === PACIENTE ===
@login_required
def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'citas/paciente_list.html', {'pacientes': pacientes})

@login_required
def paciente_detail(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'citas/paciente_detail.html', {'paciente': paciente})

@login_required
def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nuevo Paciente'})

@login_required
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

@login_required
def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'citas/confirm_delete.html', {'obj': paciente, 'type': 'Paciente'})


# === MÉDICO ===
@login_required
def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'citas/medico_list.html', {'medicos': medicos})

@login_required
def medico_detail(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    return render(request, 'citas/medico_detail.html', {'medico': medico})

@login_required
def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nuevo Médico'})

@login_required
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

@login_required
def medico_delete(request, pk):
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'citas/confirm_delete.html', {'obj': medico, 'type': 'Médico'})


# === CITA ===
@login_required
def cita_list(request):
    citas = Cita.objects.select_related('paciente', 'medico').all()
    return render(request, 'citas/cita_list.html', {'citas': citas})

@login_required
def cita_detail(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'citas/cita_detail.html', {'cita': cita})

@login_required
def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cita_list')
    else:
        form = CitaForm()
    return render(request, 'citas/form.html', {'form': form, 'title': 'Nueva Cita'})

@login_required
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

@login_required
def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('cita_list')
    return render(request, 'citas/confirm_delete.html', {'obj': cita, 'type': 'Cita'})


# === REGISTRO DE USUARIOS (ACTIVIDAD DE AUTENTICACIÓN) ===
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente tras registrarse
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'citas/register.html', {'form': form})