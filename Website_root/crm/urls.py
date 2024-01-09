from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView, Register
from django.conf import settings

urlpatterns = [
      path('', include('django.contrib.auth.urls')), 
      path('register/', Register.as_view(), name='register'),
      path('login/', CustomLoginView.as_view(), name='login'),
]
