"""
Routes for the frontend app
"""

from django.urls import path
from users.views.authentication import CustomPasswordResetDoneView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),    
    
    # Password Reset Functionality
    path("password-reset-done/", CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
]
