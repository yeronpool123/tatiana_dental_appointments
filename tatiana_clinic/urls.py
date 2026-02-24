from django.contrib import admin
from django.urls import path, include
from appointments import views

urlpatterns = [
    # Django Browser Reload
    path('__reload__/', include('django_browser_reload.urls')),

    path('admin/reports/', views.reports_dashboard, name='reports_dashboard'),

    # Admin
    path('admin/', admin.site.urls),

    # Autenticación con django-allauth
    path('accounts/', include('allauth.urls')),

    # App de citas
    path('', include('appointments.urls')),

    # App de historial médico
    path('history/', include('history.urls')),

    # Registro manual (además de allauth)
    path('register/', views.register_view, name='register'),

    # Redirección post-login según rol
    path('post-login/', views.post_login_router, name='post_login'),

    # Panel y funciones del paciente
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/profile/', views.patient_profile_edit, name='patient_profile_edit'),
    path('patient/book/', views.patient_book, name='patient_book'),
    path('patient/appointments/', views.patient_appointments, name='patient_appointments'),
]
