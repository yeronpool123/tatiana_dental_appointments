from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),

    # Citas
    path('book/', views.book_appointment, name='book_appointment'),
    path('my/', views.my_appointments, name='my_appointments'),
    path('cancel/<int:pk>/', views.cancel, name='cancel'),

    # LOGIN / LOGOUT manual
    path('login/', views.login_view, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # Redirección post-login
    path('post-login/', views.post_login_router, name='post_login'),

    # API: horarios disponibles
    path('get-available-slots/', views.get_available_slots, name='get_available_slots'),

    # Cambiar estado (solo admin)
    path("set-status/<int:pk>/<str:status>/", views.set_status, name="set_status"),

    path("services/", views.services, name="services"),

    # 🔑 NUEVA RUTA: login facial para admin
    path("admin-face-login/", views.face_login_view, name="face_login"),
]