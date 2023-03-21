from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','content')
admin.site.register(Contact,ContactAdmin)