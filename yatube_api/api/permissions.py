from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsUserOrAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.author == request.user
