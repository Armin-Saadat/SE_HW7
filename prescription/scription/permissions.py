from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-national-code', None) is not None


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-role', None) == 'doctor'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.headers.get('x-role', None) == 'admin'
