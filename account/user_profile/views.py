from datetime import datetime

from django.contrib.auth.models import update_last_login
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, \
    ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, UserRole
from .serializers import UserSignUpSerializer, ProfileSerializer


class SingUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def create(self, request, *args, **kwargs):
        signup_serializer = self.serializer_class(data=request.data)
        signup_serializer.is_valid(raise_exception=True)
        user = signup_serializer.save()
        refresh = RefreshToken.for_user(user)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, user)

        return Response(
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=HTTP_201_CREATED
        )


class AuthorizeView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        if request.user.is_anonymous:
            return Response(status=HTTP_200_OK)
        return Response(
            headers={
                'x-name': request.user.first_name,
                'x-national-code': request.user.username,
                'x-role': 'admin' if request.user.is_superuser else request.user.role,
            },
            status=HTTP_200_OK,
        )


class RetrieveUpdateMyProfileAPIView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class RetrieveProfileAPIView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    lookup_field = "username"


class ListDoctorAPIView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(role=UserRole.DOCTOR)


class ListPatientAPIView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.filter(role=UserRole.PATIENT)


class PatientCount(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return Response(data=User.objects.filter(role=UserRole.PATIENT, date_joined__gte=today).count())


class DoctorCount(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return Response(data=User.objects.filter(role=UserRole.DOCTOR, date_joined__gte=today).count())
