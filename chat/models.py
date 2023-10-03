from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from chat.functions import pick_random_image



# Create your models here.
class Chat(models.Model):
    created_at = models.DateField(default=date.today)
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    time_created = models.TimeField(auto_now_add=True, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,  related_name='chat_message_set', default=None , blank=True, null=True )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    base64_image = models.TextField(blank=True, null=True)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Bild aus dem Pool auswählen und als Base64 kodieren
        random_image = pick_random_image()  # Implementieren Sie die pick_random_image-Funktion
        UserProfile.objects.create(user=instance, base64_image=random_image)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
