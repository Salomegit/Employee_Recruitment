from django.contrib import messages

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import AddJobForm, ApplicationForm
from notification.utilities import create_notification

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Create your views here.
def approve_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.method == 'POST':
            status = request.POST.get('status')
            if status == 'approved':
                application.status = 'approved'
                application.save()
                # return a response indicating that the application has been approved
            elif status == 'declined':
                application.status = 'declined'
                application.save()
                # return a response indicating that the application has been declined
        # return a response indicating that the form was not submitted correctly
            print(status)
        # return a response indicating that the user is not authorized to approve this application

def job_pdf(request):
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3",

    # ]
    jobs = Job.objects.all()
    lines = []

    for job in jobs:
        lines.append("All jobs added by Employer") # type: ignore
        lines.append("======================")
        lines.append(job.title.encode('utf-8')) # type: ignore
        lines.append(str(job.created_at)) # type: ignore
        lines.append(job.skillset_required.encode('utf-8')) # type: ignore
        lines.append(job.about_job.encode('utf-8'))# type: ignore
        lines.append(job.experience.encode('utf-8'))# type: ignore
        lines.append(job.salary.encode('utf-8'))# type: ignore
        lines.append(job.deadline.encode('utf-8'))# type: ignore
        lines.append(job.department_name.encode('utf-8')) # type: ignore
        lines.append("======================") # type: ignore

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save() 
    buf.seek(0)


    return FileResponse(buf, as_attachment=True, filename="job.pdf")

def search(request):
    return render(request, "search.html")

def delete_application(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.delete()
    return redirect("dashboard")


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
   

    return render(request, 'job_detail.html', {'job': job, 'userprofile':request.user.userprofile})
from django.shortcuts import render, redirect
from .models import Application

def approve_job_application(request, application_id):
    application = Application.objects.get(id=application_id)
    application.status = Application.APPROVED
    application.save()
    messages.info(
            request,
            "Application Accepted...")
    return redirect('view_application', application_id=application_id)

def decline_job_application(request, application_id):
    application = Application.objects.get(id=application_id)
    application.status = Application.DECLINED
    application.save()
    messages.info(
            request,
            "Application declined...")
    return redirect('view_application', application_id=application_id)

def search_jobs(request):
  status = request.GET.get('status', '')
  job_id = request.GET.get('job_id', '')



  if job_id:
        job = Job.objects.get(id=job_id)
        if status:
            applications = job.applications.filter(status=status) # type: ignore
        else:
            applications = job.applications.all() # type: ignore
  else:
        if status:
            applications = Application.objects.filter(status=status)
        else:
            applications = Application.objects.all()
#   if status:
#     applications = Application.objects.filter(status=status)
#   else:
#     applications = Application.objects.all()
#     messages.info(
#             request,
#             "Found Results...")
  context = {
    'applications': applications,
    'status': status
  }

  return render(request, 'search_job.html', context)

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)
   
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
    
      

        if form.is_valid():
            email = form.cleaned_data['email']
            if Application.objects.filter(job=job, email=email).exists():
                messages.info(request, 'This email has already been used to apply for this job')

                return redirect('job:apply_for_job')

            else:
                application = form.save(commit=False)
                application.job = job
                application.created_by = request.user
                application.resume = request.FILES["resume"]
                application.save()
                messages.success(request, 'Applied successfully.')
                create_notification(request, job.created_by, 'application', extra_id=application.id)
                return redirect("dashboard")
        # if form.is_valid():
        #     application = form.save(commit=False)
        #     application.job = job
        #     application.created_by = request.user
        #     application.resume = request.FILES["resume"]
            
            
        #     application.save()
        #     messages.info(
        #     request,
        #     "Applied successfully...")
        #     create_notification(request,
        #                         job.created_by,
        #                         'application',
        #                         extra_id=application.id)

        #     return redirect("dashboard")
 
    else:
        form = ApplicationForm()
    context = {
       
        'form': form,
        'job': job
    }
    return render(request, 'apply_for_job.html', context)


@login_required
def add(request):

    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.image = request.FILES['image']
            
            job.save()
            messages.info(
            request,
            "Job Added successfully...")

            return redirect("dashboard")

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
            messages.info(
            request,
            "Job Edited successfully...")
            return redirect("dashboard")

            

    else:
        form = AddJobForm(instance=job)

    return render(request, 'edit_job.html', {'form': form,'job':job})


@login_required
def edit_app(request,application_id):
    application = get_object_or_404(Application,pk=application_id,created_by=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST,instance=application)

        if form.is_valid():
            application = form.save(commit=False)
            
            application.save()
            messages.info(
            request,
            "Application Edited successfully...")
            return redirect("dashboard")
        

            
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'edit_application.html', {'form': form,'application':application})