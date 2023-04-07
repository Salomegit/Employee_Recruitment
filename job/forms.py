from django import forms
from .models import Job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','skillset_required','about_job','experience','salary','deadline', 'department_name','image']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name','last_name','date_of_birth','gender','education','email','location','content','experience','mobile', 'resume']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Application.objects.filter(email=email).exists():
            raise forms.ValidationError('This email has already been used to apply for a job.')
        return email