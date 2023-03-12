import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    jobslist = []
    data = json.loads(request.body)
    query =  data['query']
    department_name  = ['department_name']

    jobs = Job.objects.filter(Q(title__icontains=query) | Q(skillset_required__icontains=query) | Q(about_job__icontains=query) )

    if department_name:
        jobs = jobs.filter(department_name = department_name)


    for job in jobs:
        obj = {
            "id": job.id,
            "title":job.title,
            "url": "/jobs/%s/" % job.id

        }
        print(jobs)
        jobslist.append(obj)

    return JsonResponse ( {'jobs': jobslist} )
