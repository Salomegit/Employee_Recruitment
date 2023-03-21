from django.contrib import admin
from .models import Userprofile, ConversationMessage
# Register your models here.
class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('application','created_by','content','created_at')

admin.site.register(Userprofile)
admin.site.register(ConversationMessage,ConversationMessageAdmin)