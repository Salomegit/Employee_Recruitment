from django.urls import path
from . import views


app_name = "userprofile"

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    
    ]