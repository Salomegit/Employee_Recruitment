from django.contrib import admin
from .models import Job
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)



admin.site.register(Job, JobAdmin)