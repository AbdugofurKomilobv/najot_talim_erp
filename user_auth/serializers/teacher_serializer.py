from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import *



class UserSer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ('id','username')

class TeacherRegisterSerializer(serializers.ModelSerializer):
    user = UserSer()
    course = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ('id','user','departments','course','descriptions')

    def get_course(self,obj):
         if obj.course.exists():
              return [course.title for course in obj.course.all()]
         return ["Xozirda biriktirilgan kurs mavjud emas"]
       

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



