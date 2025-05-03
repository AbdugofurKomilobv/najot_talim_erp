from django.shortcuts import render
from student.serializers import StudentListSerializer
from student.student_l_models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from user_auth.models import GroupStudent, Teacher


from functools import wraps




# Custom Decorator: Faqat autentifikatsiya qilingan foydalanuvchiga ruxsat berish
def is_authenticated_user(func):
    @wraps(func)
    def inner(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Autentifikatsiya talab qilinadi!"}, status=status.HTTP_401_UNAUTHORIZED)
        return func(self, request, *args, **kwargs)
    return inner

class StudentListView(APIView):
    @is_authenticated_user  # Custom Decoratorni ishlatish
    def get(self, request):
        # Teacher modelini userga mos qilib olish
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher topilmadi!"}, status=status.HTTP_404_NOT_FOUND)
        
        # Guruhni olish
        group = teacher.group
        
        # Guruhdagi o'quvchilarni olish
        student_in_group = StudentListModel.objects.filter(group=group)
        
        # Serializer orqali o'quvchilarni formatlash
        serializer = StudentListSerializer(student_in_group, many=True)

        # Javobni qaytarish
        return Response({
            "success": True,
            "message": "O'quvchilar ro'yxati",
            "o'quvchilar": serializer.data
        })
