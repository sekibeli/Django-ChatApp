from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Chat, Message, UserProfile


class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','author','text','receiver','created_at')
    list_display = ('created_at','author', 'text','receiver')
    search_fields = ('text',)
    
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
   
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    
    
# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)