from pathlib import Path
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Llave secreta (usa .env en producción)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-change-this-for-prod")

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".trycloudflare.com",  # acepta cualquier subdominio de trycloudflare.com
]

CSRF_TRUSTED_ORIGINS = [
    "https://*.trycloudflare.com",  # habilita todos los subdominios de trycloudflare
]



INSTALLED_APPS = [
    # Apps de Django
    
    'history',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tu app
    'appointments',
    'theme.apps.ThemeConfig',

    'django_browser_reload',

    # 🔐 Autenticación con allauth
    'django.contrib.sites',          # requerido por allauth
    'allauth',
    'allauth.account',


]

# Necesario para allauth
SITE_ID = 1

TAILWIND_APP_NAME = 'theme'

# Tema oscuro, variables, tailwind.config
INTERNAL_IPS = ["127.0.0.1"]

NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # requerido por allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Recarga automática
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'tatiana_clinic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # requerido por allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tatiana_clinic.wsgi.application'

# -----------------------------
# BASE DE DATOS: PostgreSQL
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "tatiana_db"),
        'USER': os.getenv("DB_USER", "tatiana_user"),
        'PASSWORD': os.getenv("DB_PASSWORD", "yeronpool1998"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': os.getenv("DB_PORT", "5432"),
        'ATOMIC_REQUESTS': True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es'  # ajustado a español
TIME_ZONE = 'America/Guayaquil'  # ajustado a tu zona
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔐 LOGIN / LOGOUT
LOGIN_REDIRECT_URL = '/patient/dashboard/'
LOGIN_URL = '/accounts/login/' # a dónde va si no está logueado
LOGOUT_REDIRECT_URL = '/login/' # a dónde va después de cerrar sesión

# -----------------------------
# AUTENTICACIÓN
# -----------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # login normal
    'allauth.account.auth_backends.AuthenticationBackend',  # login con allauth
]

# -----------------------------
# CONFIGURACIÓN DE ALLAUTH
# -----------------------------
# Métodos de login permitidos (usuario y/o email)
ACCOUNT_LOGIN_METHODS = {"email", "username"}

# Campos requeridos en el registro (el * indica obligatorio)
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']

# Email es obligatorio
ACCOUNT_EMAIL_REQUIRED = True

# Verificación de email (puede ser 'none', 'optional', 'mandatory')
ACCOUNT_EMAIL_VERIFICATION = "none"

# Límite de intentos fallidos de login (ejemplo: 5 intentos cada 60 segundos)
ACCOUNT_RATE_LIMITS = {
    "login_failed": "5/60s"
}

# -----------------------------
# 📧 Configuración de correo para reset de contraseña
# -----------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "tu_correo@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "tu_app_password")  # usa App Password de Gmail
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
