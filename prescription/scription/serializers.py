import requests
from rest_framework import serializers

from scription.models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['patient_national_id', 'doctor_national_id', 'drug_list', 'comment']
        readonly_fields = ['doctor_national_id']

    def validate_patient_national_id(self, patient_national_id):
        resp = requests.get(f"http://gateway/users/profile/{patient_national_id}/")
        if resp.status_code != 200 or resp.json().get('role') != 'patient':
            raise serializers.ValidationError("patient does not exist.")
        return patient_national_id

    def create(self, validated_data):
        self.Meta.model.objects.create(
            **validated_data,
            doctor_national_id=self.context['request'].headers.get("x-national-code")
        )