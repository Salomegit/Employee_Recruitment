from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)

    email = models.EmailField(blank=True, unique=True, null=True)
    content = models.TextField(null=True,blank=True)


