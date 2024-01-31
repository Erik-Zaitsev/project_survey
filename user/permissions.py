from rest_framework import permissions


class IsSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True