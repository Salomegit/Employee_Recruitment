from django.urls import path
from . import views


app_name = "userprofile"

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("view_application/<int:application_id>/", views.view_application , name="view_application"),

    ]