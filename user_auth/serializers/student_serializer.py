from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from ..models import *

from django.contrib.auth.hashers import make_password




class StudentGroupSerializer(serializers.ModelSerializer):
     class Meta:
          model = GroupStudent
          fields = ('id','title','course')
class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number']  
# get uchun yozilgan  serializer
class StudentRegisterSerializer(serializers.ModelSerializer):
    group = StudentGroupSerializer(many = True)
    user = UserShortSerializer(read_only = True)
    class Meta():
        model = Student
        fields = ('id','user','group','is_line','descriptions')



        

class StudentRSerializer(serializers.ModelSerializer):
     class Meta:
        model = Student
        fields = ('id','group','is_line','descriptions')

          

class StudentUserSerializer(serializers.ModelSerializer):
        is_active = serializers.BooleanField(read_only = True)
        is_staff = serializers.BooleanField(read_only = True)
        is_teacher = serializers.BooleanField(read_only = True)
        is_admin = serializers.BooleanField(read_only = True)
        is_student = serializers.BooleanField(read_only = True)

        class Meta:
             model = User
             fields = (
                       'id', 'phone_number', 'username', 'password', "email", 'is_active', 'is_staff', "is_teacher", 'is_admin', 'is_student')

# post uchun yozilgan serializer
class StudentPostSerializer(serializers.Serializer):
     user = StudentUserSerializer()
     student = StudentRSerializer()