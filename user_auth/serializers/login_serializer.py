from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from ..models import *




class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')


        try:
            user = User.objects.get(phone_number=phone_number)

        except User.DoesNotExist:
            raise serializers.ValidationError({
                'success': False,
                'detail': 'User does not exist'
            })
        
        auth_user = authenticate(phone_number=user.phone_number, password=password)
        if auth_user is None:
            raise serializers.ValidationError({
                 'success': False,
                'detail': 'Username or password is invalid' 
            })
        attrs['user']=auth_user
        return attrs
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'phone_number', 'username', 'password', "email", 'is_active', 'is_staff', "is_teacher", 'is_admin', 'is_student')


# class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    re_new_password = serializers.CharField(required=True, write_only=True)

    def update(self, instance, validated_data):

        instance.password = validated_data.get('password', instance.password)

        if not validated_data['new_password']:
            raise serializers.ValidationError({'new_password': 'not found'})

        if not validated_data['old_password']:
            raise serializers.ValidationError({'old_password': 'not found'})

        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError({'old_password': 'wrong password'})

        if validated_data['new_password'] != validated_data['re_new_password']:
            raise serializers.ValidationError({'passwords': 'passwords do not match'})

        if validated_data['new_password'] == validated_data['re_new_password'] and instance.check_password(
                validated_data['old_password']):
            instance.set_password(validated_data['new_password'])
            instance.save()
            return instance

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 're_new_password']


class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField()


# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'descriptions']


# class DepartmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departments
#         fields = ['id', 'title', 'is_active', 'descriptions']


# class WorkerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Worker
#         fields = ["id", 'user', 'departments', 'course', 'descriptions']


# class RoomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rooms
#         fields = ['id', 'title', 'descriptions']


# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupStudent
#         fields = ['id', 'title', 'course', 'teacher', "table", 'start_date', 'end_date', 'price', 'descriptions']


# class DaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Day
#         fields = ['id', 'title', 'descriptions']


# class TableTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TableType
#         fields = ['id', 'title', 'descriptions']


# class TableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Table
#         fields = ['id', 'start_time', 'end_time', 'room', 'type', 'descriptions']


# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'user', 'group', 'course', 'is_line', 'descriptions']


# #
# class TopicsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Topics
#         fields = ['id', 'title', 'course', 'descriptions']


# class GroupHomeWorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupHomeWork
#         fields = ['id', 'group', 'topic', 'is_active', 'descriptions']


# class HomeWorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HomeWork
#         fields = ['id', 'groupHomeWork', 'price', 'student', 'link', 'is_active', 'descriptions']


# class AttendanceLevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AttendanceLevel
#         fields = ['id', 'title', 'descriptions']