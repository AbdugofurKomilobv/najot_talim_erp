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
from django.shortcuts import get_object_or_404
# maxalliy importlar
from .make_token import *

from ..serializers import *


class StudentRegisterView(APIView):
    def get(self,request,id=None):
        data = {'success':True}
        if id:
            student = get_object_or_404(Student, id=id)
            serializer = StudentRegisterSerializer(student)
            data['student'] = serializer.data
        else:
            
            student = Student.objects.all()
            serializer = StudentRegisterSerializer(student,many = True)
            data['student']= serializer.data
        return Response(data=data)
    
    @swagger_auto_schema(request_body=StudentPostSerializer)
    def post(self,request):
        data = {'success':True}
        user = request.data['user']
        student = request.data['student']
        phone_number = user['phone_number']
        user_serializer = StudentUserSerializer(data = user)

        if user_serializer.is_valid(raise_exception=True):
            user_serializer.validated_data['is_student'] = True
            user_serializer.validated_data['password'] = make_password(user_serializer.validated_data.get('password'))
            user_instance = user_serializer.save()

            student_serializer_1 = StudentRSerializer(data = student)
            if student_serializer_1.is_valid(raise_exception=True):
                student_serializer_1.save(user=user_instance)
                data['user'] = user_serializer.data
                data['student'] = student_serializer_1.data
                return Response(data=data,status=status.HTTP_201_CREATED)
            return Response(data=student_serializer_1.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(data=user_serializer.errors)
    


    @swagger_auto_schema(request_body=StudentPostSerializer)
    def put(self,request,id):
        student = get_object_or_404(Student,id=id)
        user = student.user
        user_data = request.data.get('user')
        student_data = request.data.get('student')

        user_serializer = StudentUserSerializer(user,data= user_data)
        student_serializerr = StudentRSerializer(student, data = student_data)

        if user_serializer.is_valid(raise_exception=True) and student_serializerr.is_valid(raise_exception=True):
            if 'password' in user_serializer.validated_data:
                user_serializer.validated_data['password'] = make_password(user_serializer.validated_data.get('password'))
            user_serializer.save()
            student_serializerr.save()
            return Response({
                    "success":True,
                    'user':user_serializer.data,
                    'student':student_serializerr.data
                })
        return Response({"error": 'Validation fieled'},status.HTTP_400_BAD_REQUEST)
        
