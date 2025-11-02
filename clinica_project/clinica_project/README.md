#  Sistema de Gestión de Citas Médicas

Este proyecto es una aplicación web desarrollada con Django que permite gestionar pacientes, médicos y citas médicas.

##  Avance del Proyecto

El sistema ya permite:

-  Registrar, listar, editar y eliminar **pacientes**, **médicos** y **citas**.
-  Visualizar detalles individuales de cada registro.
-  Validar y guardar datos mediante formularios basados en modelos.
-  Navegación intuitiva con enlaces entre vistas (lista → detalle → edición → eliminación).
-  Base de datos actualizada con migraciones aplicadas correctamente.

Este avance sienta las bases para futuras funcionalidades como autenticación de usuarios, asignación de citas con validación de disponibilidad y generación de reportes.

---

> *Desarrollado por: [Grupo Insano #4]*  
> *Fecha: 25 de octubre de 2025*


## Actividades Implementadas

### Actividad 1 – Sistema de Autenticación
Se ha integrado completamente el módulo de autenticación de usuarios, permitiendo:
- Iniciar sesión con credenciales válidas.
- Cerrar sesión de forma segura.
- Redirección automática al *dashboard* tras el inicio de sesión.
- Registro de nuevos usuarios mediante un formulario adaptado a la identidad visual del sistema.

Se utilizaron tanto vistas genéricas de Django como formularios personalizados (`UserCreationForm`, `AuthenticationForm`) ajustados al diseño del proyecto.

### Actividad 2 – Aplicación de Bootstrap 5
Se diseñó una interfaz moderna y coherente aplicando **Bootstrap 5** en todas las plantillas:
- Creación de una **plantilla base (`base.html`)** con estructura general, menú de navegación y pie de página.
- Implementación de un **navbar responsive** con enlaces a las principales secciones (Pacientes, Médicos, Citas, etc.).
- Uso consistente de clases de Bootstrap: `container`, `form-control`, `btn`, `card`, `alert`, entre otras.
- Aplicación de una **paleta de colores profesional** (verde médico, grises oscuros, modo oscuro suave) para reforzar la identidad del sistema clínico.

### Actividad 3 – Control de Acceso y Permisos
Todas las vistas internas están protegidas:
- Se aplicó el decorador `@login_required` en cada vista que requiere autenticación.
- Los usuarios no autenticados son redirigidos automáticamente a la página de inicio de sesión.
- Se ha establecido la base para la futura implementación de **roles de usuario** (administrador, médico, paciente), preparando el modelo y la lógica necesaria para extensiones próximas.

---

## Internacionalización
El sistema está configurado en **español** como idioma predeterminado mediante la configuración de internacionalización de Django:

> *Desarrollado por: [Grupo Insano #4]*  
> *Fecha: 2 de noviembre de 2025*