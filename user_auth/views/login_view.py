# django imporlar
from django.shortcuts import render
import random
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
# rest imporlar
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
# maxalliy importlar
from .make_token import *

from ..serializers import *


class PhoneSendOTP(APIView):
    @swagger_auto_schema(request_body=SMSSerializer)
    def post(self, request, *args, **kvargs):
        phone_number = request.data.get('phone_number')
        print(phone_number)

        if phone_number:
            phone = str(phone_number)
            user = User.objects.filter(phone_number__iexact=phone)

            if user.exists():
                return Response({
                    'status': False,
                    'detail': 'phone number already exist'
                }, status=status.HTTP_400_BAD_REQUEST)

            else:
                key = send_otp()
                print("============",key)
                if key:
                    cache.set(phone_number, key, 600)
                    return Response({"message": "SMS sent successfully"}, status=status.HTTP_200_OK)
                return Response({"message": "Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)

        # 🛠 Agar phone_number kelmagan bo‘lsa — bu yerga tushadi:
        return Response({
            "status": False,
            "detail": "phone_number maydoni talab qilinadi"
        }, status=status.HTTP_400_BAD_REQUEST)




def send_otp():
    otp = str(random.randint(1001,9999))
    return otp






class VerifySms(APIView):
    pagination_class = PageNumberPagination

    @swagger_auto_schema(request_body=VerifySMSSerializer)
    def post(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            cached_code = str(cache.get(phone_number))
            if verification_code == str(cached_code):
                return Response({
                    'status': True,
                    'detail': 'OTP matched. please proceed for registration'
                })
            else:
                return Response({
                    'status': False,
                    'detail': 'otp INCOORECT'
                })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user login qiladi
class LoginApi(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
         
        
        user = serializer.validated_data.get("user")
        token = get_tokens_for_user(user)
        token["is_admin"]= user.is_admin
        

        return Response(data=token,status=status.HTTP_200_OK)