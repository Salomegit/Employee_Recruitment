from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import AddJobForm, ApplicationForm
# Create your views here.


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
            application.save()

            return redirect("users:dashboard")

    else:
        form = ApplicationForm()

    return render(request, 'apply_for_job.html', {'form': form, 'job': job})


@login_required
def add(request):

    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            # job.image = request.FILES['images']
            job.save()

            return redirect("users:dashboard")

            # return HttpResponse('added a job succesfully')
            # return http ('login')

    else:
        form = AddJobForm()

    return render(request, 'add_job.html', {'form': form})
