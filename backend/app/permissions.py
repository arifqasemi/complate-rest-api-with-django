from rest_framework import permissions
class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        admin = bool(request.user and request.user.is_staff)
        # return request.method =="GET" or admin
        return admin
    


    def has_object_permission(self, request, view, obj):
       if request.method in permissions.SAFE_METHODS:
        return True
    # Check permissions for read-only request
       else:
        return obj.user_review == request.user