from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from ..models import *





class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id','departments','course','descriptions')

class TeacherUserSerializer(serializers.ModelSerializer):
        is_active = serializers.BooleanField(read_only = True)
        is_staff = serializers.BooleanField(read_only = True)
        is_teacher = serializers.BooleanField(read_only = True)
        is_admin = serializers.BooleanField(read_only = True)
        is_student = serializers.BooleanField(read_only = True)

        class Meta:
             model = User
             fields = (
                       'id', 'phone_number', 'username', 'password', "email", 'is_active', 'is_staff', "is_teacher", 'is_admin', 'is_student')


class TeacherPostSerializer(serializers.Serializer):
    user = TeacherUserSerializer()
    teacher = TeacherRegisterSerializer()



