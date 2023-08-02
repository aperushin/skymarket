from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsOwner(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsAdmin(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN
