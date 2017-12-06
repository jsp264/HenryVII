#
# Models.py
#
# The main goal here is to make our models of Tutor, Review, and Prespective 
# Development focused on making the Tutor first and then slowly building how
# the tutor wanted to present themselves. 
#
# Author: jsp264
# Updated: 12/3/2017


# Create your models here.

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Tutor(models.Model):
    screen_name         = models.CharField(max_length=100)
    teaching_start_date = models.DateTimeField('start date')
    teacher_email       = models.EmailField(max_length=200)
    teacher_address     = models.CharField(max_length=100)
    tutor_photo         = models.ImageField(upload_to = 'teachers/%Y/%m')
    alma_mater          = models.CharField(max_length=100)
    degree              = models.CharField(max_length=100)
    major               = models.CharField(max_length=50)
    years_xp            = models.PositiveIntegerField()

    def __str__(self):
        return self.screen_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.teaching_start_date <= now

class Seeker(models.Model):
    seek_name         = models.CharField(max_length=100)
    join_date         = models.DateTimeField('join_date')
    seekemail         = models.EmailField(max_length=200)
    is_parent         = models.BooleanField()
    seek_addr         = models.CharField(max_length=200)
    desired_subjects  = models.CharField(max_length=250)
    seek_photo        = models.ImageField(upload_to = 'seekers/%Y/%m')

    def __str__(self):
        return self.seek_name


class Specialty(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    spec_text = models.CharField(max_length=200)
    desc_text = models.CharField(max_length=500)

    def __str__(self):
        return self.spec_text