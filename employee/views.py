from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from job.models import Job
# Create your views here.
@login_required
def base(request):
    jobs = Job.objects.all()[0:3]
    return render(request ,"base.html",{'jobs':jobs})


def register(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email= request.POST.get('email')
        password= request.POST.get('password')
        name = request.POST.get("username")
        
        new_user = User.objects.create_user(name,email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()

        return redirect("employee:login")

        
    return render(request ,"register.html",locals())

def Login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=name, email= email, password=password) 
        if user is not None:
            login(request, user) 
            return redirect("employee:base") 
        else:
            return HttpResponse('Error user does not exist')
    return render(request ,"login.html",)

def logoutuser(request):
    logout(request)
    return redirect("employee:login")



 