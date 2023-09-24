from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_at','author', 'text','receiver')
    fields = ('author','text','receiver','created_at')
    search_fields = ('text',)
# Register your models here.
admin.site.register(Message, MessageAdmin)