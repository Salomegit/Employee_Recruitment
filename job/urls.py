from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .api import api_search

app_name = "job"

urlpatterns = [
    path("api/search",api_search,name = "api_search"),
    path("search/",views.search,name = "search"),
    path("<int:job_id>/edit", views.edit, name="edit"),
    path("<int:application_id>/edit_app", views.edit_app, name="edit_app"),
    path("search_jobs", views.search_jobs, name="search_jobs"),

    path("<int:job_id>", views.job_detail, name="job_detail"),
    path("job/add" ,views.add, name="add"),
    path("<int:job_id>/apply_for_job/" ,views.apply_for_job, name="apply_for_job "),
    path("delete_application/<int:application_id>",views.delete_application,name="delete_application"),
    path("job_pdf",views.job_pdf,name="job_pdf"),
    path('job-application/<int:application_id>/approve/', views.approve_job_application, name='approve_job_application'),
    path('job-application/<int:application_id>/decline/', views.decline_job_application, name='decline_job_application'),

    ]



urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)