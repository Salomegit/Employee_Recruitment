from django.urls import path
from employee import views


app_name = "employee"

urlpatterns = [
    path("base", views.base, name="base"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("register", views.register, name="register"),
    path("logout",views.logoutuser,name="logout"),
    path("login", views.Login, name="login"),
    # patterns(r'^images/(?P<path>.*)$', 'django.views.static.serve',
    #              {'document_root': settings.MEDIA_ROOT}),
              
    ]