from django.db import models

class Prescription(models.Model):
    patient_national_code = models.CharField(max_length=10)
    doctor_national_code = models.CharField(max_length=10)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment
