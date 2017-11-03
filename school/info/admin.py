# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Teacher,Student,Course
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)