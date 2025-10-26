# citas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # === VISTA DE INICIO ===
    path('', views.home, name='home'),

    # === PACIENTES ===
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/<int:pk>/', views.paciente_detail, name='paciente_detail'),
    path('pacientes/nuevo/', views.paciente_create, name='paciente_create'),
    path('pacientes/<int:pk>/editar/', views.paciente_update, name='paciente_update'),
    path('pacientes/<int:pk>/eliminar/', views.paciente_delete, name='paciente_delete'),

    # === MÉDICOS ===
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/<int:pk>/', views.medico_detail, name='medico_detail'),
    path('medicos/nuevo/', views.medico_create, name='medico_create'),
    path('medicos/<int:pk>/editar/', views.medico_update, name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.medico_delete, name='medico_delete'),

    # === CITAS ===
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/<int:pk>/', views.cita_detail, name='cita_detail'),
    path('citas/nueva/', views.cita_create, name='cita_create'),
    path('citas/<int:pk>/editar/', views.cita_update, name='cita_update'),
    path('citas/<int:pk>/eliminar/', views.cita_delete, name='cita_delete'),
]