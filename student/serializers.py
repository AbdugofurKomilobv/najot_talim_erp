from rest_framework import serializers
from student.student_l_models import *



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentListModel
        fields = ('student', 'group', 'date', 'is_present', 'arrival_time', 'izox')
