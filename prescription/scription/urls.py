from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.get_all_prescriptions, name='all'),
]
