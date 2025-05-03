# user_auth/admin.py
from django.contrib import admin
from .student_l_models import StudentListModel

@admin.register(StudentListModel)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'date', 'is_present', 'arrival_time', 'izox')
    list_filter = ('group', 'date', 'is_present')
    search_fields = ('student__user__full_name',)
