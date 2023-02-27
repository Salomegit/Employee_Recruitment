from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


GENDER = (('M', 'Male'), ('F', 'Female') )



class Job(models.Model):

    CHOICES_SIZE =   ( ('CSS', 'Computer Support Specialist'),
    ('HWA' , 'Hardware Engineer'),
    ('CSA' , 'Computer System Analyst '),
    ('SWD' , 'Software Developer'),
    ('PRG','Programmer'),
    ('WBD','Web developer',),
    ('NWE','Network engineer'),
    ('SWT', 'Software Tester'))

    
      


    


    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    skillset_required = models.TextField(max_length=2000)
    about_job = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to="covers/")
    experience = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=50,null=True)
    deadline = models.CharField(max_length=50,null=True)

    department_name = models.CharField( max_length=3,choices=CHOICES_SIZE)

    
    created_by = models.ForeignKey(User,
                                   related_name="jobs",
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
        
    class Meta:
        ordering = ['-created_at']
        
    def application_count(self):
        return Application.objects.filter(job=self).values('user').distinct().count()
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
    
    