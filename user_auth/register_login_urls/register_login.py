from django.urls import path
from django.urls import include
from ..views import *


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# user_auth urls
urlpatterns = [
    
    path('register/',RegisterUserApi.as_view()),

     path('token/', LoginApi.as_view(), ),


     
]