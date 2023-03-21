from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from users.models import Userprofile
from job.models import Job
from employee.models import Contact

# Create your views here.
# @login_required
def base(request):
    jobs = Job.objects.all()[0:8]
    return render(request, "base.html", {'jobs': jobs})

def about(request):
    return render (request,'about.html')

def contact(request):
    if request.method == "POST":
        cfull_name=request.POST.get("full_name")
        cemail=request.POST.get("email")
        ccontent=request.POST.get("content")
        query=Contact(full_name=cfull_name,email=cemail,content=ccontent)
        query.save()
        messages.info(request,"Thanks for contacting us we will get back to you soon...")
        return redirect("employee:contact")
    return render (request,'contact.html')

def help(request):
    return render (request,'help.html')

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
            'jobseeker'
        )
        if account_type == 'employer':
            userprofile = Userprofile.objects.create(user=user,
                                                     is_employer=True)
            userprofile.save()

            return redirect("users:dashboard")
 
        else:
            userprofile = Userprofile.objects.create(user=user)
            userprofile.save()
      
        login(request, user)
        messages.info(request,"Sign-up successful")

        return redirect("users:dashboard")
    else:

      return render(request, "register.html", locals())






def Login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        # email = request.POST.get('email')
        password = request.POST.get('password')

        user1 = authenticate(request,
                            username=name,
                            # email=email,
                            password=password)
        if user1 is not None:
            login(request, user1)
            message = "Login successful!"

            return render(request,"base.html",{'message':message})
            
        else:
            message1 = "Invalid username or password"
            return render(request,"login.html",{'message1':message1})


    return render(
        request,
        "login.html",
    )


def logoutuser(request):
    logout(request)
    return redirect("employee:base")
