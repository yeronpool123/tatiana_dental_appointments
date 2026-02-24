from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment, generate_time_slots_for_date
from history.models import ClinicalHistory
from django.db.models import Count 
from django.shortcuts import render 
from appointments.models import Appointment 
from django.contrib.auth.models import User





# VISTA DE SERVICIOS
def services(request):
    return render(request, "partials/services.html")


#-----------------------------
# REPORTES Y ESTADÍSTICAS
# -----------------------------
@login_required
def reports_dashboard(request):
    """Estadísticas de citas"""
    total_citas = Appointment.objects.count()
    citas_confirmadas = Appointment.objects.filter(status='confirmada').count()
    citas_canceladas = Appointment.objects.filter(status='cancelada').count()
    citas_pendientes = Appointment.objects.filter(status='pendiente').count()
    
    # Pacientes registrados
    total_pacientes = User.objects.count()
    
    context = {
        'total_citas': total_citas,
        'citas_confirmadas': citas_confirmadas,
        'citas_canceladas': citas_canceladas,
        'citas_pendientes': citas_pendientes,
        'total_pacientes': total_pacientes,
    }
    return render(request, 'admin/reports.html', context)



# -----------------------------
# VERIFICACIÓN DE HISTORIA CLÍNICA ANTES DE AGENDAR CITA
# -----------------------------
@login_required
def book_appointment(request):
    """Agendar cita validando historia clínica primero."""
    if not ClinicalHistory.objects.filter(patient=request.user).exists():
        messages.warning(request, "Debes registrar tu historia clínica antes de agendar una cita.")
        return redirect('add_history')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.user = request.user
            try:
                ap.save()
            except ValidationError as e:
                for msg in e.messages:
                    form.add_error(None, msg)
                return render(request, 'patient/book.html', {'form': form})
            messages.success(request, 'Cita agendada correctamente.')
            return redirect('my_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'patient/book.html', {'form': form})


# -----------------------------
# AUTENTICACIÓN
# -----------------------------
def login_view(request):
    """Login manual (además de allauth)."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_login')
        else:
            return render(request, 'registration/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'registration/login.html')

def cerrar_sesion(request):
    """Logout manual."""
    logout(request)
    return redirect('login')

def register_view(request):
    """Registro manual de usuario (además de allauth)."""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Este correo ya está registrado")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=username,
            password=password
        )

        messages.success(request, "Cuenta creada correctamente")
        return redirect('login')

    return render(request, 'registration/register.html')

# -----------------------------
# HOME
# -----------------------------
def home(request):
    """Página principal: welcome si no está autenticado, base si es admin."""
    if not request.user.is_authenticated:
        return render(request, 'welcome.html')

    query = request.GET.get('q', '')
    appointments = Appointment.objects.order_by('start')

    if query:
        appointments = appointments.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(cedula__icontains=query)
        )

    return render(request, 'base.html', {
        'appointments': appointments,
        'query': query
    })

# -----------------------------
# ADMINISTRACIÓN DE CITAS
# -----------------------------
def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def set_status(request, pk, status):
    """Cambiar estado de cita (solo admin)."""
    appointment = get_object_or_404(Appointment, pk=pk)

    if status not in ["pending", "confirmed", "cancelled"]:
        messages.error(request, "Estado inválido.")
        return redirect('my_appointments')

    appointment.status = status
    appointment.save()
    messages.success(request, f"Estado actualizado a {status}.")
    return redirect('my_appointments')

# -----------------------------
# CITAS DEL USUARIO
# -----------------------------
@login_required
def my_appointments(request):
    """Listado de citas del usuario autenticado."""
    appointments = Appointment.objects.filter(user=request.user).order_by('start')
    return render(request, 'appointments/my_appointments.html', {
        'appointments': appointments
    })

@login_required
def cancel(request, pk):
    """Cancelar cita del usuario autenticado."""
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    appointment.delete()
    messages.success(request, "Cita cancelada correctamente.")
    return redirect('my_appointments')

# -----------------------------
# API: HORARIOS DISPONIBLES
# -----------------------------
def get_available_slots(request):
    """API: obtener horarios disponibles para una fecha."""
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({"error": "Fecha no proporcionada. Usa ?date=YYYY-MM-DD"}, status=400)

    try:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"error": "Formato de fecha inválido. Usa YYYY-MM-DD"}, status=400)

    try:
        slot_minutes = int(request.GET.get('slot', 30))
    except ValueError:
        slot_minutes = 30

    all_slots_dt = generate_time_slots_for_date(selected_date, slot_minutes=slot_minutes)
    taken_qs = Appointment.objects.filter(start__date=selected_date)
    taken_set = set(t.start.strftime("%H:%M") for t in taken_qs)

    available = [dt.strftime("%H:%M") for dt in all_slots_dt if dt.strftime("%H:%M") not in taken_set]
    return JsonResponse({"available_slots": available})

# -----------------------------
# PACIENTE: PANEL Y PERFIL
# -----------------------------
@login_required
def post_login_router(request):
    """Redirige según rol tras login."""
    user = request.user
    if user.is_staff:  # si es admin/staff
        return redirect('/admin/')
    else:  # si es paciente normal
        return redirect('patient_dashboard')

@login_required
def patient_dashboard(request):
    """Panel principal del paciente."""
    profile = getattr(request.user, 'patient_profile', None)
    return render(request, 'patient/dashboard.html', {'profile': profile})

@login_required
def patient_profile_edit(request):
    """Editar perfil del paciente."""
    profile = request.user.patient_profile
    if request.method == 'POST':
        profile.phone = request.POST.get('phone', '')
        profile.birth_date = request.POST.get('birth_date') or None
        profile.insurance = request.POST.get('insurance', '')
        profile.emergency_contact = request.POST.get('emergency_contact', '')
        profile.notes = request.POST.get('notes', '')
        profile.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('patient_dashboard')
    return render(request, 'patient/profile_edit.html', {'profile': profile})

@login_required
def patient_book(request):
    """Agendar cita desde panel paciente."""
    return book_appointment(request)  # reutiliza la lógica de book_appointment

@login_required
def patient_appointments(request):
    """Listado de citas del paciente."""
    appointments = Appointment.objects.filter(user=request.user).order_by('-start')
    return render(request, 'patient/appointments.html', {'appointments': appointments})
