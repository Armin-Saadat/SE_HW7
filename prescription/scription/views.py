import logging

from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Prescription

from .permissions import IsAuthenticated, IsAdmin, IsDoctor
from .serializers import PrescriptionSerializer

class ListPrescription(ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        logging.info(self.request.headers)
        role = self.request.headers.get("x-role")
        national_code = self.request.headers.get("x-national-code")
        if role == 'admin':
            return Prescription.objects.all()
        elif role == 'doctor':
            return Prescription.objects.filter(doctor_national_code=national_code)
        elif role == 'patient':
            return Prescription.objects.filter(patient_national_code=national_code)
        else:
            return Prescription.objecst.none()


class CreatePrescription(CreateAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated, IsDoctor]
