from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "job"

urlpatterns = [
    path("job/<int:job_id>", views.job_detail, name="job_detail"),
    path("job/add" ,views.add, name="add"),
    path("<int:job_id>/apply_for_job" ,views.apply_for_job, name="apply_for_job ")

    ]



urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)