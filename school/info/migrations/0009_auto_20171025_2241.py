# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-26 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20171025_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_course_test',
            new_name='student_course',
        ),
    ]