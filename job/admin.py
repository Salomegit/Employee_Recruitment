from click import File
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Job, Application,ApplicationSummary
from django.db.models import Count, Sum, Case, When, IntegerField, F

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title','created_at','status','created_by')
    list_filter = ('department_name',)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job','first_name','last_name','location','resume','status')
    list_filter = ('job','status')

@admin.register(ApplicationSummary)
class ApplicationSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/application_summary_change_list.html'
    date_hierarchy = 'created_at'

    # ...

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        metrics = {
            'total': Count('id'),
            'total_selected': Sum(Case(When(status='approved', then=1), default=0, output_field=IntegerField())),
            'total_rejected': Sum(Case(When(status='declined', then=1),default=0 ,output_field=IntegerField())),
            # 'percent_selected': Cast(100.0 * Sum(Case(When(status='accepted', then=1), default=0, output_field=IntegerField())) / Count('id'), FloatField()),
            # 'percent_rejected': Cast(100.0 * Sum(Case(When(status='declined', then=1), default=0, output_field=IntegerField())) / Count('id'), FloatField()),
              'percent_selected': 100.0 * F('total_selected') / F('total'),
              'percent_rejected': 100.0 * F('total_rejected') / F('total'),
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
       .filter(total__gt=0)  # exclude jobs with 0 applications

        .order_by('-total')
          )
        return response














admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.unregister(Group)