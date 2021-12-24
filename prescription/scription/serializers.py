import requests
from rest_framework import serializers

from scription.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['patient_national_code', 'doctor_national_code', 'drug_list', 'comment']
        read_only_fields = ['doctor_national_code']

    def validate_patient_national_code(self, patient_national_code):
        resp = requests.get(f"http://gateway/profile/{patient_national_code}/")
        if resp.status_code != 200 or resp.json().get('role') != 'patient':
            raise serializers.ValidationError("patient does not exist.")
        return patient_national_code

    def create(self, validated_data):
        return self.Meta.model.objects.create(
            **validated_data,
            doctor_national_code=self.context['request'].headers.get("x-national-code")
        )