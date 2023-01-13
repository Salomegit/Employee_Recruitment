from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from userprofile.models import Userprofile
from job.models import Job


# Create your views here.
@login_required
def base(request):
    jobs = Job.objects.all()[0:8]
    return render(request, "base.html", {'jobs': jobs})

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')


def register(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get("username")

        user = User.objects.create_user(name, email, password)
        user.first_name = fname
        user.last_name = lname

        user.save()
        account_type = request.POST.get(
            'account_type',
            'jobseeker',
        )
        if account_type == 'employer':
            userprofile = Userprofile.objects.create(user=user,
                                                     is_employer=True)
            userprofile.save()

            return redirect("userprofile:dashboard")

        else:
            userprofile = Userprofile.objects.create(user=user)
            userprofile.save()
      
        login(request, user)

        return redirect("userprofile:dashboard")
    else:

      return render(request, "register.html", locals())


# def Login(request):
#     if request.method == "POST":
#         name = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user1 = authenticate(request,
#                             username=name,
#                             email=email,
#                             password=password)
#         if user1 is not None:
#             login(request, user1)
#             return redirect("employee:base")
            
#         else:
#             return HttpResponse('Error user does not exist')
#     return render(
#         request,
#         "login.html",
#     )


def logoutuser(request):
    logout(request)
    return redirect("employee:register")
