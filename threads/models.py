# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings

# Create your models here - Title called subject for a specfic post
class Subject(models.Model):
 
    name = models.CharField(max_length=255) # will create field called name
    description = HTMLField() # will have the description  - django-tinymce
 
    def __unicode__(self):
        return self.name
        
"""  Create a new thread with certain fields in it  """     
class Thread(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)  # when it got created 
 
"""  Create a new thread with certain fields in it  """  
class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)