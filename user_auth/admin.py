from django.contrib import admin

from .models import *

# User lar
admin.site.register(User)
# O'qtuvchilar
admin.site.register(Teacher)

admin.site.register(Departments)
# O'quvchilar
admin.site.register(Student)



