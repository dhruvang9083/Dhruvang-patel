# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.TextField(max_length=50)),
                ('student', models.TextField(max_length=50)),
                ('course', models.TextField(max_length=50)),
            ],
        ),
    ]
