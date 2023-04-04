from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


GENDER = (('M', 'Male'), ('F', 'Female') )



class Job(models.Model):

    

    COMPUTER_SUPPORT_SPECIALIST = 'Computer Support Specialist'
    HARDWARE_ENGINEER = 'Hardware Engineer'
    COMPUTER_SYSTEM_ANALYST = 'Computer System Analyst'
    SOFTWARE_DEVELOPER = 'Software Developer'
    PROGRAMMER = 'Programmer'
    WEB_DEVELOPER = 'Web Developer'
    NETWORK_ENGINEER = 'Network Engineer'
    SOFTWARE_TESTER = 'Software Tester'
    FRONTEND_DEVELOPER = "Frontend Developer"
    BACKEND_DEVELOPER = "Backend Developer"

    CHOICES_SIZE =   ( (COMPUTER_SUPPORT_SPECIALIST ,'COMPUTER_SUPPORT_SPECIALIST'),
    ( HARDWARE_ENGINEER ,'HARDWARE_ENGINEER'),
    ( COMPUTER_SYSTEM_ANALYST, 'COMPUTER_SYSTEM_ANALYST' ),
    ( SOFTWARE_DEVELOPER, 'SOFTWARE_DEVELOPER'),
    ( PROGRAMMER , 'PROGRAMMER'),
    ( WEB_DEVELOPER,'WEB_DEVELOPER'),
    ( NETWORK_ENGINEER,'NETWORK_ENGINEER'),
    ( SOFTWARE_TESTER,'SOFTWARE_TESTER'),
    (FRONTEND_DEVELOPER,"FRONTEND_DEVELOPER"),
    (BACKEND_DEVELOPER,"BACKEND_DEVELOPER")
    )

      
    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    
    CHOICES_STATUS = (
        (EMPLOYED,'Employed'),
        (ACTIVE,'Active' ),
        (ARCHIVED,'Archived' )
     )

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    skillset_required = models.TextField(null=True)
    about_job= models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="covers/",null=True,blank=True)
    experience = models.CharField(max_length=100,null=True)
    salary = models.CharField(max_length=50,null=True)
    deadline = models.CharField(max_length=50,null=True)

    department_name = models.CharField( max_length=30,choices=CHOICES_SIZE)

    
    created_by = models.ForeignKey(User,
                                   related_name="jobs",
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=CHOICES_STATUS,default='active')
    
    def __str__(self):
        return self.title
    
        
    class Meta:
        ordering = ['-created_at']

    
class Application(models.Model):

    APPROVED = 'approved'
    PENDING = 'pending'
    DECLINED = 'declined'

    
    CHOICES_STATUS = (
        (APPROVED,'Approved'),
        (PENDING,'Pending' ),
        (DECLINED,'Declined' )
     )
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
    education   = models.CharField( max_length=2553, null=True, blank=True)



    content = models.TextField()
    experience = models.TextField()
    
    resume  = models.FileField( upload_to="resumes/", null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=False)
    status = models.CharField(max_length=20,choices=CHOICES_STATUS,default='pending')

    created_by = models.ForeignKey(User,
                                   related_name="applications",
                                   on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

class ApplicationSummary(Application):
        class Meta:
          proxy = True
        verbose_name = 'Application Summary'
        verbose_name_plural = 'Application Summary'