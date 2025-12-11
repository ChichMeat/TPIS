from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Собака'),
        ('cat', 'Кошка'),
        ('rabbit', 'Кролик'),
        ('bird', 'Птица'),
        ('other', 'Другое'),
    ]
    
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=50, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_species_display()})"

class Veterinarian(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Др. {self.full_name}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class DoctorSchedule(models.Model):
    doctor = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ['doctor', 'date']

    def __str__(self):
        return f"{self.doctor.full_name} - {self.date}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Запланирован'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменен'),
    ]
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Veterinarian, on_delete=models.PROTECT, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    schedule = models.ForeignKey(DoctorSchedule, on_delete=models.PROTECT)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    symptoms = models.TextField(blank=True)
    diagnosis = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Прием #{self.id}: {self.pet.name} -> {self.doctor.full_name}"
