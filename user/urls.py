from django.urls import path, include
from django.contrib import admin
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView, RegisterApi #authenticate_user
from rest_framework_jwt.views import obtain_jwt_token
from .serializers import *
from .models import *

urlpatterns = [
	path('update/', UserRetrieveUpdateAPIView.as_view()),
	#path('admin/', admin.site.urls),
	#path('login/', authenticate_user),
	#path('signup/', RegisterApi.as_view()),
]	 	