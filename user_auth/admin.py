from django.contrib import admin

from .models import *



admin.site.register([Teacher,User,Course,Departments,GroupStudent,Student])
admin.site.register([Table,Rooms,TableType])



