# citas/models.py

from django.db import models

class CentroMedico(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, default="Sin dirección")
    telefono = models.CharField(max_length=15, blank=True, default="")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Centro Médico"
        verbose_name_plural = "Centros Médicos"


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_especialidad

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"


class Paciente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100, blank=True, default="")
    telefono = models.CharField(max_length=15, blank=True, default="")
    correo = models.EmailField(max_length=100, blank=True, default="")  # ← corregido
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=True, default="")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True, default="")
    correo = models.EmailField(max_length=100, blank=True, default="")  # ← corregido
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    centro_medico = models.ForeignKey(CentroMedico, on_delete=models.SET_NULL, null=True, blank=True)
    numero_licencia = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"


class Cita(models.Model):
    ESTADO_CHOICES = [
        ('programada', 'Programada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=100, blank=True, default="")  # ← ¡agregado default!
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='programada')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita {self.id} - {self.paciente} con {self.medico}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"


class Usuario(models.Model):
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('paciente', 'Paciente'),
        ('medico', 'Médico'),
    ]

    nombre_usuario = models.CharField(max_length=30, unique=True)
    contrasena = models.CharField(max_length=100)  # ⚠️ En producción usa `AbstractUser` o `set_password()`
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    paciente = models.OneToOneField(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    medico = models.OneToOneField(Medico, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_usuario

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"