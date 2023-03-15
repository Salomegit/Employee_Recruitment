from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import AddJobForm, ApplicationForm
from notification.utilities import create_notification

# Create your views here.
def search(request):
    return render(request, "search.html")

def delete_application(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.delete()
    return redirect("users:dashboard")


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
   

    return render(request, 'job_detail.html', {'job': job})


@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.resume = request.FILES["resume"]
            
            
            application.save()

            # create_notification(request,
            #                     job.created_by,
            #                     'application',
            #                     extra_id=application.id)

            return redirect("users:dashboard")

    else:
        form = ApplicationForm()

    return render(request, 'apply_for_job.html', {
            'form': form,
            'job': job
        })


@login_required
def add(request):

    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            
            job.save()

            return redirect("users:dashboard")

            # return HttpResponse('added a job succesfully')
            # return http ('login')

    else:
        form = AddJobForm()

    return render(request, 'add_job.html', {'form': form})


@login_required
def edit(request,job_id):
    job = get_object_or_404(Job,pk=job_id,created_by=request.user)
    if request.method == 'POST':
        form = AddJobForm(request.POST,instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            
            job.save()

            return redirect("users:dashboard")

            # return HttpResponse('added a job succesfully')
            # return http ('login')

    else:
        form = AddJobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form,'job':job})


