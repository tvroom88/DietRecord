#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
import datetime
from django.utils.timezone import utc


# Create your models here.

class DietProgram(models.Model):
    time = models.DateField(auto_now_add=True)
    sitUpCount = models.IntegerField()
    pushUpCount = models.IntegerField()

class DietProgramAdmin(admin.ModelAdmin):
    list_display = ('time', 'sitUpCount', 'pushUpCount')


admin.site.register(DietProgram, DietProgramAdmin)