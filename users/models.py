from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    
User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0]) # type: ignore



def __str__(self):
    return self.user