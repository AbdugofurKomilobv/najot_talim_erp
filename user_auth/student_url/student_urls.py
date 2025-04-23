from django.urls import path
from django.urls import include
from ..views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# user_auth urls
urlpatterns = [
 
     path('student_register/',StudentRegisterView.as_view()),
     path('student_register/<int:id>/',StudentRegisterDetailView.as_view()),

     
     
]