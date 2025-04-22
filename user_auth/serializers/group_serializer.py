from rest_framework import serializers
from ..models import *

class GroupStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupStudent
        fields = "__all__"

    
        
class GroupTitleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = ['title']

class GroupFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = '__all__'


# ViewSetlar uchun
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class TableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableType
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'



