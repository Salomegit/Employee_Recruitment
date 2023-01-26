from django.contrib import admin
from .models import Userprofile, ConversationMessage
# Register your models here.

admin.site.register(Userprofile)
admin.site.register(ConversationMessage)