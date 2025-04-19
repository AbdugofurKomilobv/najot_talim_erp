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


# User ro'yxatga olish
class RegisterUserApi(APIView):
    pagination_class = PageNumberPagination

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response({
                'status': True,
                'datail': 'Account create',
                'data': serializer.data     
            })
    
    def get(self, request):
        users = User.objects.all().order_by('-id')
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)

# Teacher ro'yxatdan o'tqazish
class TeacherRegisterView(APIView):
    def get(self,request):
        data = {'success':True}
        teacher = Teacher.objects.all()
        serializer = TeacherRegisterSerializer(teacher,many = True)
        data["teacher"] = serializer.data
        return Response(data=data)

    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def post(self,request):
        data = {'success':True}
        user = request.data['user']
        teacher = request.data['teacher']
        phone_number = user['phone_number']
        user_serializer = TeacherUserSerializer(data=user)


        if  user_serializer.is_valid(raise_exception=True):
            user_serializer.validated_data['is_teacher'] = True
            user_serializer.validated_data['is_active'] =True
            user_serializer.validated_data['password'] = make_password(user_serializer.validated_data.get('password'))
            user = user_serializer.save()


            teacher_serializer = TeacherRegisterSerializer(data = teacher)
            if teacher_serializer.is_valid(raise_exception=True):
                
                teacher_serializer.save(user=user)
                data['user'] = user_serializer.data
                data['teacher'] = teacher_serializer.data
                return Response(data=data)
            return Response(data=teacher_serializer.errors)
        return Response(data=user_serializer.errors) 



