from django.db import models
from django.contrib.auth.models import User


GENDER = (('M', 'Male'), ('F', 'Female') )



class Job(models.Model):

    SIZE_1_9 = 'size_1-9'
    SIZE_10_49 = 'size_10-49'
    SIZE_50_99 = 'size_50-99'
    SIZE_100 = 'size_100'

    CHOICES_SIZE = (
        (SIZE_1_9 ,'1-9'),
        (SIZE_10_49 ,'10-49'),
        (SIZE_50_99 ,'50-99'),
        (SIZE_100 ,'100+'),


    )


    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    skillset_required = models.TextField(max_length=200)
    about_job = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to="covers/")
    experience = models.CharField(max_length=50,null=True)
    salary = models.CharField(max_length=50,null=True)
    deadline = models.CharField(max_length=50,null=True)

    company_name = models.CharField(max_length=255, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_zipcode = models.CharField(max_length=255, blank=True, null=True)
    company_place = models.CharField(max_length=255, blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_9)

    
    created_by = models.ForeignKey(User,
                                   related_name="jobs",
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Application(models.Model):

    job = models.ForeignKey(Job,
                            related_name='applications',
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER,
                              blank=False,
                              null=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    location = models.CharField(
        max_length=104,
        null=True
    )
    mobile = models.IntegerField(null=True, blank=True)
    education   = models.CharField( max_length=255, null=True, blank=True)



    content = models.TextField()
    experience = models.TextField()
    
    # resume  = models.FileField( upload_to='resumes/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=False)

    created_by = models.ForeignKey(User,
                                   related_name="applications",
                                   on_delete=models.CASCADE)
    

    