# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0002_auto_20170914_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
