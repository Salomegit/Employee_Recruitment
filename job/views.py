from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required 
from .models import Job
from .forms import AddJobForm,ApplicationForm
# Create your views here.

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'job_detail.html',{'job':job})

@login_required
def apply_for_job(request,job_id):
    job = Job.objects.get(pk=job_id) 

    if request.method == 'POST':
        form = ApplicationForm(request.Post)
       
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()
            
        return redirect("userprofile:dashboard")

    else:
        form = ApplicationForm()
    return render(request,'apply_for_job.html',{'form':form,'job':job})


@login_required
def add(request):
    if request.method == "POST":
        form = AddJobForm(request.Post,request.FILES)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            
            return redirect("userprofile:dashboard")

            # return HttpResponse('added a job succesfully')
            # return http ('login')

    else:
        form = AddJobForm()
    return render (request,'add_job.html',{'form':form})