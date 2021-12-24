from django.urls import path

from .views import ListPrescription, CreatePrescription, PrescriptionCount

urlpatterns = [
    path('', ListPrescription.as_view(), name='all'),
    path('create/', CreatePrescription.as_view(), name='create'),
    path('count/', PrescriptionCount.as_view(), name='count'),
]
