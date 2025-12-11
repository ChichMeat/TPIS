from django.contrib import admin
from .models import Client, Pet, Veterinarian, Service, Appointment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email']
    search_fields = ['full_name', 'phone']

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'owner']
    list_filter = ['species']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet', 'doctor', 'appointment_time', 'status']
    list_filter = ['status', 'appointment_time']

admin.site.register(Veterinarian)
admin.site.register(Service)
