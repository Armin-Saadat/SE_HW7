import logging
from datetime import datetime

from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework.response import Response

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


class PrescriptionCount(GenericAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return Response(data=Prescription.objects.filter(created_at__gte=today).count())
