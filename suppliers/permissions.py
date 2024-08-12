from rest_framework.permissions import BasePermission


class IsActiveStaff(BasePermission):
    """
    Разрешает доступ только активным штатным пользователям.
    """

    def has_permission(self, request, view) -> bool:
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.is_staff
        )
