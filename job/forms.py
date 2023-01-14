from django import forms
from .models import Job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','skillset_required','about_job','image']

# class ApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Application
#         field = []