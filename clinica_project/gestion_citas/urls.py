# app_citas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.paciente_list, name='paciente_list'),
]