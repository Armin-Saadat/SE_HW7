from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.get_all_prescriptions, name='all'),
    path('<str:national_code>/patient/', views.get_patient_prescriptions, name='patient'),
    path('<str:national_code>/doctor/', views.get_doctor_prescriptions, name='doctor'),
]
