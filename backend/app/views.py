from django.http import JsonResponse
from .models import Client, Pet, Appointment
import json

def create_appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Логика создания записи
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_doctors(request):
    doctors = Doctor.objects.all()
    data = [{'id': d.id, 'name': d.name, 'specialization': d.specialization} for d in doctors]
    return JsonResponse({'doctors': data})
