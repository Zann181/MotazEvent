# MotazEvent 🎉

> Sistema integral de gestión de eventos con control de ventas de barra y tickets digitales mediante códigos QR

## 📋 Descripción

MotazEvent es una plataforma web responsive que facilita la gestión completa de eventos, desde la creación y promoción hasta el control de acceso y ventas en tiempo real. El sistema genera tickets digitales con códigos QR únicos para cada cliente, permitiendo un control eficiente de entradas y consumos en la barra del evento.

**Ideal para:** Organizadores de eventos, bares, discotecas, festivales, conferencias y cualquier establecimiento que requiera control de acceso y gestión de ventas.

## ✨ Características Principales

- **📱 Diseño Responsive**: Adaptable a cualquier dispositivo (móvil, tablet, desktop)
- **🎫 Tickets Digitales**: Generación automática de códigos QR únicos por cliente
- **📊 Gestión de Eventos**: Creación, edición y control completo de eventos
- **💰 Control de Ventas**: Sistema de punto de venta para la barra del evento
- **📧 Envío Automático**: Distribución de tickets vía email con código QR
- **🔍 Escaneo QR**: Validación de entrada mediante lectura de códigos QR
- **📈 Reportes en Tiempo Real**: Dashboard con estadísticas de ventas y asistencia
- **👥 Gestión de Clientes**: Base de datos de asistentes y historial de compras
- **🔐 Autenticación Segura**: Sistema de roles (admin, staff, cajero)

## 🛠️ Stack Tecnológico

### Backend
- **Framework**: Django 4.x
- **Lenguaje**: Python 3.8+
- **ORM**: Django ORM
- **API REST**: Django REST Framework (opcional)

### Frontend
- **Templates**: Django Templates
- **CSS Framework**: Bootstrap 5 / Tailwind CSS
- **JavaScript**: Vanilla JS / jQuery
- **Responsive Design**: Mobile-first approach

### Funcionalidades Especiales
- **QR Generation**: python-qrcode / qrcode
- **Email Service**: Django Email Backend / SendGrid
- **PDF Generation**: ReportLab / WeasyPrint
- **Database**: PostgreSQL / SQLite (desarrollo)

## 🚀 Instalación

### Prerrequisitos

```bash
# Versiones requeridas
Python 3.8 o superior
pip (gestor de paquetes de Python)
virtualenv (recomendado)
PostgreSQL (producción) o SQLite (desarrollo)
```

### Configuración del Entorno

1. **Clona el repositorio:**
```bash
git clone https://github.com/Zann181/MotazEvent.git
cd MotazEvent
```

2. **Crea y activa el entorno virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configura las variables de entorno:**
```bash
cp .env.example .env
```

Edita el archivo `.env` con tu configuración:
```env
SECRET_KEY=tu_secret_key_super_segura
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/motazevent
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu_email@gmail.com
EMAIL_HOST_PASSWORD=tu_password
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Ejecuta las migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crea un superusuario:**
```bash
python manage.py createsuperuser
```

7. **Recopila archivos estáticos:**
```bash
python manage.py collectstatic
```

8. **Inicia el servidor de desarrollo:**
```bash
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000`

## 📁 Estructura del Proyecto

```
MotazEvent/
├── motazevent/              # Configuración principal del proyecto
│   ├── settings.py          # Configuraciones de Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuración WSGI
│
├── events/                  # App de gestión de eventos
│   ├── models.py            # Modelos (Event, Ticket, Cliente)
│   ├── views.py             # Vistas y lógica de negocio
│   ├── forms.py             # Formularios de Django
│   ├── urls.py              # URLs de la app
│   └── templates/           # Templates HTML
│
├── bar/                     # App de control de barra
│   ├── models.py            # Modelos (Producto, Venta, Orden)
│   ├── views.py             # Sistema de POS
│   └── templates/           # Templates de barra
│
├── tickets/                 # App de gestión de tickets
│   ├── models.py            # Modelos de tickets y QR
│   ├── qr_generator.py      # Generación de códigos QR
│   └── email_service.py     # Envío de tickets por email
│
├── static/                  # Archivos estáticos
│   ├── css/                 # Estilos personalizados
│   ├── js/                  # JavaScript
│   └── img/                 # Imágenes
│
├── media/                   # Archivos subidos
│   ├── qr_codes/            # Códigos QR generados
│   └── event_images/        # Imágenes de eventos
│
├── templates/               # Templates globales
│   ├── base.html            # Template base
│   └── components/          # Componentes reutilizables
│
├── requirements.txt         # Dependencias del proyecto
├── manage.py                # CLI de Django
└── README.md                # Este archivo
```

## 🎯 Uso del Sistema

### Panel de Administración

Accede al panel admin en `http://localhost:8000/admin`

**Roles disponibles:**
- **Superadmin**: Control total del sistema
- **Organizador**: Crear y gestionar eventos
- **Staff**: Escanear QR y validar entradas
- **Cajero**: Gestión de ventas en barra

### Flujo de Trabajo

1. **Crear Evento**
   - Accede al panel de eventos
   - Completa información (nombre, fecha, lugar, capacidad)
   - Configura precios de entradas
   - Publica el evento

2. **Venta de Tickets**
   - El cliente completa formulario de compra
   - Sistema genera código QR único
   - Ticket se envía automáticamente al email del cliente

3. **Control de Acceso**
   - Staff escanea código QR en entrada
   - Sistema valida y registra el acceso
   - Actualiza contador de asistencia en tiempo real

4. **Gestión de Barra**
   - Cajero escanea QR del cliente
   - Registra consumos asociados al ticket
   - Sistema actualiza totales de venta

### Comandos Útiles

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar tests
python manage.py test

# Recopilar archivos estáticos
python manage.py collectstatic

# Limpiar sesiones expiradas
python manage.py clearsessions
```

## 🔧 Configuración Avanzada

### Configurar Email SMTP (Gmail)

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_app_password'
```

### Configurar PostgreSQL

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'motazevent_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Modelos Principales

```python
# Ejemplo de modelo Event
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='event_images/')
    is_active = models.BooleanField(default=True)

# Ejemplo de modelo Ticket
class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    qr_code = models.ImageField(upload_to='qr_codes/')
    unique_code = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
```

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas de una app específica
python manage.py test events

# Ejecutar con cobertura
coverage run --source='.' manage.py test
coverage report
```

## 🚀 Despliegue

### Preparación para Producción

1. **Configura las variables de entorno de producción:**
```env
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
SECRET_KEY=clave_super_segura_aleatoria
```

2. **Configura archivos estáticos:**
```bash
python manage.py collectstatic --noinput
```

3. **Usa Gunicorn como servidor WSGI:**
```bash
pip install gunicorn
gunicorn motazevent.wsgi:application --bind 0.0.0.0:8000
```

### Opciones de Hosting

- **Heroku**: Deploy fácil con Git
- **DigitalOcean**: VPS con Django
- **AWS EC2**: Escalabilidad enterprise
- **PythonAnywhere**: Hosting específico para Django
- **Railway**: Deploy moderno y rápido

## 🤝 Contribución

Las contribuciones son bienvenidas y apreciadas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Add: descripción del cambio'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Convenciones de Código

- Seguir PEP 8 para código Python
- Usar nombres descriptivos en español para variables
- Documentar funciones complejas
- Escribir tests para nuevas funcionalidades
- Mantener templates organizados y reutilizables

## 📝 Roadmap

- [x] Sistema base de gestión de eventos
- [x] Generación y envío de tickets QR
- [x] Control de ventas de barra
- [ ] App móvil nativa (Android/iOS)
- [ ] Integración con pasarelas de pago (Stripe, PayPal)
- [ ] Sistema de notificaciones push
- [ ] Dashboard analítico avanzado
- [ ] Integración con redes sociales
- [ ] Sistema de fidelización de clientes
- [ ] Multi-idioma (i18n)
- [ ] API REST completa
- [ ] Escaneo QR offline

## 🐛 Problemas Conocidos

Si encuentras algún bug, por favor repórtalo en [Issues](https://github.com/Zann181/MotazEvent/issues)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Zann** - [@Zann181](https://github.com/Zann181)

- 💼 LinkedIn: [Tu perfil](https://linkedin.com/in/tu-perfil)
- 📧 Email: tu-email@ejemplo.com
- 🌐 Portfolio: [tu-portfolio.com](https://tu-portfolio.com)

## 🙏 Agradecimientos

- Django Software Foundation por el increíble framework
- Comunidad de Python por las librerías de QR
- Todos los contribuidores y testers del proyecto

## 📞 Soporte

¿Tienes preguntas o necesitas ayuda?

- 📝 Abre un [Issue](https://github.com/Zann181/MotazEvent/issues)
- 💬 Inicia una [Discussion](https://github.com/Zann181/MotazEvent/discussions)
- 📧 Contacto directo: tu-email@ejemplo.com

---

⭐️ Si este proyecto te es útil, considera darle una estrella en GitHub | Hecho con ❤️ y Django
