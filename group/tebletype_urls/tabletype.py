from django.urls import path, include
from user_auth.views.group_view import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('table-types', TableTypeViewSet)

urlpatterns = [

    path('table_type/', include(router.urls)),
]