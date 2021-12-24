from django.db import models

class Prescription(models.Model):
    patient_national_code = models.CharField(max_length=10)
    doctor_national_code = models.CharField(max_length=10)
    drug_list = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
