from django.urls import path
from django.urls import include
from ..views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# user_auth urls
urlpatterns = [
    # path('post_phone_send_otp/',PhoneSendOTP.as_view()),
    # path('post_phone_verifay_otp/',VerifySms.as_view()),
    path('register/',RegisterUserApi.as_view()),
    # path('teacher_register/',TeacherRegisterView.as_view()),
     path('token/', LoginApi.as_view(), ),
    #  path('student_register/',StudentRegisterView.as_view()),
    #  path('student_register/<int:id>/',StudentRegisterView.as_view())

     
]