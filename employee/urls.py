from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path("index", views.index, name="index"),
    path("register", views.register, name="register"),

    ]