from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
	course = models.CharField(max_length = 50) 
	
	def __str__(self):
		return self.course

	def get_absolute_url(self):
		return reverse("info:disp",kwargs={'id':self.id})



class Teacher(models.Model):
	name = models.CharField(max_length = 50)
	teacher_course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.name


class Student(models.Model):
	name = models.CharField(max_length = 50)
	student_course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
	# teacher_course = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

