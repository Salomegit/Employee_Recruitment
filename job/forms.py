from django import forms
from .models import Job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','skillset_required','about_job','experience','salary','deadline']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name','last_name','date_of_birth','gender','education','email','location','content','experience',
                 'mobile']