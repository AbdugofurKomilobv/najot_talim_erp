from django.urls import path
from django.urls import include
from .views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('post_phone_send_otp/',PhoneSendOTP.as_view()),
    path('post_phone_v_otp/',VerifySms.as_view()),
    path('register/',RegisterUserApi.as_view()),
     path('token/', LoginApi.as_view(), ),
     
]