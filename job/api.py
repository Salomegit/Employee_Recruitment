import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    jobslist = []
    data = json.loads(request.body)
    query =  data['query']
    department_name  = data['department_name']
    print(f"{query}-{department_name}")
    jobs = Job.objects.filter(status=Job.ACTIVE).filter(Q(title__icontains=query) | Q(skillset_required__icontains=query) | Q(about_job__icontains=query) )
    print(jobs[0].__dict__)
    if department_name:
        jobs = jobs.filter(department_name = department_name)

    for job in jobs:
        jobslist.append({'id':job.id,
                         'title':job.title,
                         'skillset_required':job.skillset_required,
                         'about_job':job.about_job,
                         'url': '/job/%s' % job.id


                         })

    print("Found jobs are: ",len(jobslist))

    return JsonResponse ( {'jobs': jobslist })
