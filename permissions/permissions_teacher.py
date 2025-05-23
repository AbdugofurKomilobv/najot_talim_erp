from rest_framework.permissions import BasePermission

class IsTeacherOfGroupOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
    
        if request.user.is_superuser:
            return True

        
        return obj.teacher.filter(user=request.user).exists()
