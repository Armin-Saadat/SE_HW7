from django.shortcuts import render
from django.http import HttpResponse
from .models import Prescription
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def create_prescription(request):
    prescription = Prescription.objects.create(doctor_national_code=request.POST["doctor_national_code"], patient_national_code=request.POST["patient_national_code"], drug_list=request.POST["drug_list"], comment=request.POST["comment"])
    output = 'prescription created.'
    return HttpResponse(output)

