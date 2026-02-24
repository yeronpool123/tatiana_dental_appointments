from django.contrib import admin
from .models import Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','start','end','phone','cedula','user')
    list_filter = ('start',)
    search_fields = ('first_name','last_name','cedula','phone')
