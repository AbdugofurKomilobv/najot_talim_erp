from django.urls import path

from ..views import *
from  ..views import PhoneSendOTP, VerifySms

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# user_auth urls
urlpatterns = [
    path('post_phone_send_otp/',PhoneSendOTP.as_view()),
    path('post_phone_verifay_otp/',VerifySms.as_view()),
]