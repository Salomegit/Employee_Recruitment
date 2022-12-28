from django.urls import path
from . import views

app_name = "employee"

urlpatterns = [
    path("base", views.base, name="base"),
    path("register", views.register, name="register"),
    path("login", views.Login, name="login"),
    path("logout",views.logoutuser,name="logout")

    ]