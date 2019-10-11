from rest_framework.permissions import BasePermission


class PaydaAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(request.user.is_authenticated and
                    request.user.is_paydaadmin)


class PaydaSalesPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(request.user.is_authenticated and
                    request.user.is_sales)


class PaydaCommentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(request.user.is_authenticated and
                    (request.user.is_paydaadmin or request.user.is_agent))


class PaydaAgentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return bool(request.user.is_authenticated and
                    request.user.is_agent)
