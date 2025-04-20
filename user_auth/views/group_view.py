# o'zimniki 
from ..serializers import *

# swagger uchun
from drf_yasg.utils import swagger_auto_schema

# rest_framework 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class GroupStudentView(APIView):
    def get(self,request):
           data = {'success':True}
           group = GroupStudent.objects.all()
           serializer = StudentGroupSerializer(group,many =True)
           data['group'] =serializer.data
           return Response(data=data,status=status.HTTP_200_OK)
    




class RoomsViewSet(ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

class TableTypeViewSet(ModelViewSet):
    queryset = TableType.objects.all()
    serializer_class = TableTypeSerializer

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer