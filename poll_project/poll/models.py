# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PollsList(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question

class PollDetail(models.Model):
    poll = models.ForeignKey(PollsList, on_delete=models.CASCADE, default=1)
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.poll)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
