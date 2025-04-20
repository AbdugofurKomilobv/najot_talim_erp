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
    






class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField()


