from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    skillset_required = models.TextField(max_length=150)
    about_job = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/covers")

    created_by = models.ForeignKey(User, related_name="jobs",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title