from datetime import date
from django.conf import settings
from django.db import models
from django.db.models.fields import DateField

# Create your models here.

class Message(models.Model):
    text = models.charField(max_length=500)
    created_at = DateField(default=date.today)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')