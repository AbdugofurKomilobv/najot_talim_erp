# user_auth/admin.py
from django.contrib import admin
from models import StudentListModel

@admin.register(StudentListModel)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'date', 'is_present', 'arrival_time', 'note')
    list_filter = ('group', 'date', 'is_present')
    search_fields = ('student__user__full_name',)
