from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """Проверка прав доступа активного сотрудника."""
    message = "Доступно только активным сотрудникам"

    def has_permission(self, request, view):
        return request.user.is_staff and request.user.is_active
