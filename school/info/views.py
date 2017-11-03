# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . models import Course,Student,Teacher
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def teacher(req):
	all_teacher = Teacher.objects.values('name')
	all_student = Student.objects.values('name')
	print(all_student)
	return render(req,'teacher.html',{'teacher_name':all_teacher,'student_name':all_student})

def course(req,id=None):
	all_course = Course.objects.all()
	return render(req,'course.html',{'course_name':all_course})

def id_course(req,id=None):
	instance = get_object_or_404(Course,id=id)
	
	teacher_list = Teacher.objects.values('name').distinct().filter(teacher_course_id=id)
	student_list = Student.objects.values('name').distinct().filter(student_course_id=id)
	context = {
		"students":student_list,
		"teachers":teacher_list,
		"course": instance
	}
	print(teacher_list)
	return render(req,'id.html',context)