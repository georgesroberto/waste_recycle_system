"""
Routes for the frontend app
"""

from django.urls import path
from users.views.authentication import CustomPasswordResetDoneView
from .views import home

urlpatterns = [
    path("", home, name="home"),
    
    
    # Password Reset Functionality
    path("password-reset-done/", CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
]
