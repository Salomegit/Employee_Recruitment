from django import forms
from .models import Job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','skillset_required','about_job','experience','salary','deadline''company_name', 'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name','last_name','date_of_birth','gender','education','email','location','content','experience','mobile']