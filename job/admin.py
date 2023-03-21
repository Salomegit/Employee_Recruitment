from django.contrib import admin
from .models import Job, Application
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title','created_at','status','created_by')
    list_filter = ('department_name',)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','first_name','last_name','location','resume','created_at')
    list_filter = ('job',)


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)