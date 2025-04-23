from rest_framework import serializers
from models import *



class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentListModel()
        fields = "__all__"
