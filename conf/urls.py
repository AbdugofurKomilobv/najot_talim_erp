
from django.contrib import admin
from django.urls import path
from django.urls import include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('admin/', admin.site.urls),
    # User authentication
   
   path('/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
   path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   # auth user api urls
    # path('api/',include('user_auth.urls')),
    path('teacher/',include('user_auth.teacher_urls')),
    path('student/',include('user_auth.student_url')),
    path('otp/',include('user_auth.otp_urls')),
    path('register_login_user/',include('user_auth.register_login_urls')),

   
    
]