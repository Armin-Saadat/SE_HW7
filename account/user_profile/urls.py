from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SingUpView, AuthorizeView, RetrieveUpdateMyProfileAPIView, \
    ListDoctorAPIView, ListPatientAPIView, RetrieveProfileAPIView

urlpatterns = [
    path('signup/', SingUpView.as_view(), name='signup'),
    path('signin/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authorize/', AuthorizeView.as_view(), name='authorize'),
    path('profile/', RetrieveUpdateMyProfileAPIView.as_view(), name='my_profile'),
    path('profile/<int:pk>/', RetrieveProfileAPIView.as_view(), name='profile'),
    path('doctor/', ListDoctorAPIView.as_view(), name='doctor'),
    path('patient/', ListPatientAPIView.as_view(), name='patient'),
]