"""URL patterns for the reports app."""

from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path('submit/', views.submit_report, name='submit_report'),
    path('update-status/<int:report_id>/', views.update_status, name='update_status'),

]