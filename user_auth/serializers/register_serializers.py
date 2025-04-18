from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from ..models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'phone_number', 'username', 'password', "email", 'is_active', 'is_staff', "is_teacher", 'is_admin', 'is_student')
