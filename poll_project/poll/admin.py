# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import PollsList, PollDetail

admin.site.register(PollsList)
admin.site.register(PollDetail)



# python3 manage.py createsuperuser
