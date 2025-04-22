# o'zimniki 
from ..serializers import *
from permissions.permissions_teacher import IsTeacherOfGroupOrAdmin


# swagger uchun
from drf_yasg.utils import swagger_auto_schema

# rest_framework 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class GroupStudentView(APIView):
    permission_classes = [IsAuthenticated,IsTeacherOfGroupOrAdmin]
    def get(self,request):
           data = {'success':True}
           group = GroupStudent.objects.all()
           serializer = StudentGroupSerializer(group,many =True)
           data['group'] =serializer.data
           return Response(data=data,status=status.HTTP_200_OK)
    def post(self, request):
         data = {"success": True}
         serializer = GroupStudentSerializer(data = request.data)
         if serializer.is_valid(raise_exception=True):
              serializer.save()
              data['group'] = serializer.data
              return Response(data=data,status=status.HTTP_201_CREATED)
         return Response({
              "success":False,
              'errors': serializer.errors
         },status=status.HTTP_400_BAD_REQUEST)
    

class GroupStudentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherOfGroupOrAdmin]

    def get_serializer_class(self, request, group):
        if request.user.is_superuser:
            return GroupFullSerializer
        return GroupTitleUpdateSerializer

    def get(self, request, pk):
        group = get_object_or_404(GroupStudent, pk=pk)
        self.check_object_permissions(request, group)

        serializer_class = self.get_serializer_class(request, group)
        serializer = serializer_class(group)
        return Response({"success": True, "group": serializer.data})

    def put(self, request, pk):
        group = get_object_or_404(GroupStudent, pk=pk)
        self.check_object_permissions(request, group)

        serializer_class = self.get_serializer_class(request, group)
        serializer = serializer_class(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "group": serializer.data})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        group = get_object_or_404(GroupStudent, pk=pk)
        self.check_object_permissions(request, group)

        if not request.user.is_superuser:
            return Response({"detail": "Faqat admin o‘chira oladi"}, status=403)

        group.delete()
        return Response({"success": True, "message": "Group o‘chirildi"})




class RoomsViewSet(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class TableTypeViewSet(ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer