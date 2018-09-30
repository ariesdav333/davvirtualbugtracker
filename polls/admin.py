# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Poll, Vote, PollSubject

# Register your models to the admin panel so they can displayed to the user
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(PollSubject)
