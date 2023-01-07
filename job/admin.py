from django.contrib import admin
from .models import Job, Application
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)



admin.site.register(Job, JobAdmin)
admin.site.register(Application)