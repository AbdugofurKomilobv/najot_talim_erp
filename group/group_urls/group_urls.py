from django.urls import path, include
from user_auth.views.group_view import *


urlpatterns = [
    path('group/', GroupStudentView.as_view()),
    path('detail/<int:pk>/',GroupStudentDetailAPIView.as_view())

]
