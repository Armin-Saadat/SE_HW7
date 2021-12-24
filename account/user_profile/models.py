from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    PATIENT = 'patient', 'Patient'
    DOCTOR = 'doctor', 'Doctor'


class User(AbstractUser):
    # username: National Code
    # first_name: Name
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.PATIENT)

    @property
    def national_code(self):
        return self.username

    @property
    def name(self):
        return self.first_name
