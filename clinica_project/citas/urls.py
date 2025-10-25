

from django.urls import path
from . import views

urlpatterns = [
    # Pacientes
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/<int:pk>/', views.paciente_detail, name='paciente_detail'),

    # Médicos
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/<int:pk>/', views.medico_detail, name='medico_detail'),

    # Citas
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/<int:pk>/', views.cita_detail, name='cita_detail'),
]

# citas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Pacientes
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/nuevo/', views.paciente_create, name='paciente_create'),
    path('pacientes/editar/<int:pk>/', views.paciente_update, name='paciente_update'),
    path('pacientes/eliminar/<int:pk>/', views.paciente_delete, name='paciente_delete'),

    # Médicos
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/nuevo/', views.medico_create, name='medico_create'),
    path('medicos/editar/<int:pk>/', views.medico_update, name='medico_update'),
    path('medicos/eliminar/<int:pk>/', views.medico_delete, name='medico_delete'),

    # Citas
    path('citas/', views.cita_list, name='cita_list'),
    path('citas/nueva/', views.cita_create, name='cita_create'),
    path('citas/editar/<int:pk>/', views.cita_update, name='cita_update'),
    path('citas/eliminar/<int:pk>/', views.cita_delete, name='cita_delete'),
    path('pacientes/<int:pk>/', views.paciente_detail, name='paciente_detail'),
]

# citas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← Agrega esta línea
    # ... resto de tus rutas
]

# citas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/nuevo/', views.paciente_create, name='paciente_list'),
    # ... otras rutas
]