from django.urls import path
from student.views import StudentListView

urlpatterns = [
    path('student_list/attends/', StudentListView.as_view(), name='student-list'),
]
