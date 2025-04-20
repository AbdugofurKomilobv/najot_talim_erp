from django.urls import path
from django.urls import include
from ..views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# user_auth urls
urlpatterns = [

    path('teacher_register/', TeacherRegisterView.as_view()),

]