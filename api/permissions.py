from rest_framework.permissions import BasePermission, SAFE_METHODS


class MyIsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return True

class MyIsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

