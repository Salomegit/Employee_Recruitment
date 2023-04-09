from click import File
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Job, Application, ApplicationSummary
from django.db.models import Count, Sum, Case, When, IntegerField, F
from django.db.models.functions import Trunc
from django.db.models import Sum, Min, Max, F, FloatField
from datetime import datetime, timedelta
from django.db.models.functions import Trunc
from django.db.models import Sum, Min, Max, F, FloatField
from datetime import datetime, timedelta
from django.db.models import DateTimeField
from django import template
from django.utils.numberformat import format
from django import template
from django.http import HttpResponse
from django.utils.html import format_html
from django.urls import path


from django.urls import reverse

register = template.Library()






@register.filter
def sort_by_total(objects):
    return sorted(objects, key=lambda x: x.total)
@register.filter(name='custom_intcomma')
def custom_intcomma(value):
    return format(value, ',', grouping=3)

class JobAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('title', 'created_at', 'status', 'created_by')
    list_filter = ('department_name', )


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'first_name', 'last_name', 'location',
                    'status')
    list_filter = ('job', 'status')


@admin.register(ApplicationSummary)
class ApplicationSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/application_summary_change_list.html'
    date_hierarchy = 'created_at'
    list_display = ('job', 'first_name', 'last_name', 'location', 
                    'status')
    list_filter = (
        'job__title',
    )
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        metrics = {
            'total':
            Count('id'),
            'total_selected':
            Sum(
                Case(When(status='approved', then=1),
                     default=0,
                     output_field=IntegerField())),
            'total_rejected':
            Sum(
                Case(When(status='declined', then=1),
                     default=0,
                     output_field=IntegerField())),
            'total_pending':
            Sum(Case(When(status='pending', then=1), default=0, output_field=IntegerField())),

            # 'percent_selected': Cast(100.0 * Sum(Case(When(status='accepted', then=1), default=0, output_field=IntegerField())) / Count('id'), FloatField()),
            # 'percent_rejected': Cast(100.0 * Sum(Case(When(status='declined', then=1), default=0, output_field=IntegerField())) / Count('id'), FloatField()),
            'percent_selected':
            100.0 * F('total_selected') / F('total'),
            'percent_rejected':
            100.0 * F('total_rejected') / F('total'),
            'percent_pending':
            100.0 * F('total_pending') / F('total')}

        context_data = response.context_data
            
        if context_data is None:
            return response

        try:
            qs = context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        if response.context_data is not None:
            response.context_data['summary'] = list(
                qs.values('job__title').annotate(**metrics).filter(
                    total__gt=0)  # exclude jobs with 0 applications
                .order_by('-total'))

        summary_over_time = qs.annotate(period=Trunc(
            'created_at',
            'day',
            output_field=DateTimeField(),
        ), ).values('period').annotate(total=Count('id')).order_by('period')

        start_date = datetime.today() - timedelta(days=30)
        end_date = datetime.today()

        summary_over_time = summary_over_time.filter(
            created_at__range=[start_date, end_date])
        print(summary_over_time)
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        if response.context_data is not None:
         response.context_data['summary_over_time'] = [{
        'period': x['period'],
        'total': x['total'] or 0,

        'pct': (x['total'] or 0) / (high - low) * 100 if high > low else 0,
        } for x in summary_over_time]
        # response.context_data['summary_over_time'] = [{
        #      'period':
        #       x['period'],
        #      'total':
        #      x['total'] or 0,
        #      'pct': ((x['total'] or 0) - low) / (high - low) *
        #      100 if high > low else 0,
        #     } for x in summary_over_time]

        if response.context_data is not None:
            response.context_data['summary'] = list(
                qs.values('job__title').annotate(**metrics).filter(
                    total__gt=0)  # exclude jobs with 0 applications
                .order_by('-total'))

        return response
    








    


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.unregister(Group)