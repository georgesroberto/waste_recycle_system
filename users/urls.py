"""
Routing for users app
"""

from django.urls import path
from .views.authentication import (
    CustomRegisterView,
    CustomLoginView,
    CustomPasswordResetView,
    CustomPasswordResetConfirmView,
    user_logout
)

app_name = 'users'

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        CustomPasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
]
