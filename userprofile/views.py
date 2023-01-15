from django.shortcuts import render,get_object_or_404 
from django.contrib.auth.decorators import login_required
from job.models import Application
# Create your views here.
@login_required
def dashboard(request):
   return render ( request,'dashboard.html' ,{'userprofile': request.user.userprofile})

@login_required
def view_application(request, application_id):
   application = get_object_or_404(Application  , pk=application_id, created_by=request.user) 
   return render ( request,'view_application.html' ,{'application': application})

