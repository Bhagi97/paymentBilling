from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poster(models.Model):
    image = models.FileField(upload_to='posters', blank=True)
    name = models.TextField()
    uploader = models.ForeignKey(User)
    show = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)