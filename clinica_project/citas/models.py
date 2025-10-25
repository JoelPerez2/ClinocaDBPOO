from django.db import models

class CentroMedico(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre_especialidad

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nacimiento = models.DateField(null=False)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    centro_medico = models.ForeignKey(CentroMedico, on_delete=models.SET_NULL, null=True, blank=True)
    numero_licencia = models.CharField(max_length=50, unique=True) 
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

class Cita(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    motivo = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=20, null=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita {self.id} - {self.paciente.nombre} con {self.medico.nombre}"

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, null=False, unique=True)
    contrasena = models.CharField(max_length=100, null=False)
    rol = models.CharField(max_length=20, null=False)
    paciente = models.OneToOneField(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    medico = models.OneToOneField(Medico, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre_usuario
