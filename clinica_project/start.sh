#!/bin/bash
set -e  # Detener si hay algún error

# 1. Ejecutar migraciones
python manage.py migrate --noinput

# 2. Recopilar archivos estáticos (CSS, JS, imágenes)
python manage.py collectstatic --noinput

# 3. Iniciar la app con Gunicorn
gunicorn clinica_project.wsgi:application --bind 0.0.0.0:$PORT