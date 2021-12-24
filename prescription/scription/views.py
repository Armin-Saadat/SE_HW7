from django.shortcuts import render
from django.http import HttpResponse
from .models import Prescription
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the scription index.")

def get_all_prescriptions(request):
    prescriptions = Prescription.objects.all()
    output = serializers.serialize('json', prescriptions)
    return HttpResponse(output, content_type='application/json')

def get_patient_prescriptions(request, national_code):
    prescriptions = Prescription.objects.filter(patient_national_code=national_code)
    output = serializers.serialize('json', prescriptions)
    return HttpResponse(output, content_type='application/json')

def get_doctor_prescriptions(request, national_code):
    prescriptions = Prescription.objects.filter(doctor_national_code=national_code)
    output = serializers.serialize('json', prescriptions)
    return HttpResponse(output, content_type='application/json')

