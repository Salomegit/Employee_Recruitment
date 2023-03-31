from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Job, Application,ApplicationSummary
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title','created_at','status','created_by')
    list_filter = ('department_name',)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','first_name','last_name','location','resume','created_at')
    list_filter = ('job',)

@admin.register(ApplicationSummary)
class ApplicationSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/application_summary_change_list.html'
    date_hierarchy = 'created_at'

class ApplicationSummaryAdmin(admin.ModelAdmin):
    # ...

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        metrics = {
            'total': Count('id'),
            'total_selected': Sum(Case(When(status='selected', then=1), default=0, output_field=IntegerField())),
            'total_rejected': Sum(Case(When(status='rejected', then=1), default=0, output_field=IntegerField())),
        }

        context_data = response.context_data
        if context_data is None:
           return response

        try:
          qs = context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
 
        if response.context_data is not None:
          response.context_data['summary'] = list(
        qs
        .values('job__title')
        .annotate(**metrics)
        .order_by('-total')
          )
        return response








admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.unregister(Group)