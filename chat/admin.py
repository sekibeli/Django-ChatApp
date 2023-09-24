from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','author','text','receiver','created_at')
    list_display = ('created_at','author', 'text','receiver')
    search_fields = ('text',)
   
# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)