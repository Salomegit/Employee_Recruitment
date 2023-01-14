from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


GENDER = (('1', 'Male'), ('2', 'Female'))


class Job(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    skillset_required = models.TextField(max_length=200)
    about_job = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/covers")
    experience = models.CharField(max_length=50,null=True)
    salary = models.CharField(max_length=50,null=True)
    deadline = models.CharField(max_length=50,null=True)
    created_by = models.ForeignKey(User,
                                   related_name="jobs",
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):

    job = models.ForeignKey(Job,
                            related_name='applications',
                            on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10,
                              choices=GENDER,
                              blank=True,
                              null=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    location = models.CharField(
        max_length=104,
        null=True
    )
    # mobile = models.IntegerField()
    # resume = models.FileField(upload_to='resumes/')

    content = models.TextField()
    experience = models.TextField()
    
    
    created_at = models.DateTimeField(auto_now_add=True,null=False)

    created_by = models.ForeignKey(User,
                                   related_name="applications",
                                   on_delete=models.CASCADE)
