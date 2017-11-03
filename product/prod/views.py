# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm
import json
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import authenticate, login

def product(req):
	
	all_product = Product.objects.all()
	a = "All Product Details"

	return render(req,'product.html',{'ans':a , 'pro':all_product})
def disp(req):
	if not req.user.is_staff or not req.user.is_superuser:
		raise Http404
	form = ProductForm(req.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		# print form.cleaned_data.get("name")
		# print form.cleaned_data.get("price")
		# print form.cleaned_data.get("quantity")
		instance.save()
		messages.success(req,"successfully created")
		#return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(req,"not created")
	


	'''
	if req.method == "POST":
		print req.POST.get("name")
		print req.POST.get("price")
'''
	context={
	"form": form, 

	}
	return render(req,'post_form.html',context)
	
def id_product(req,id=None):
	instance = get_object_or_404(Product,id=id)
	
	s = Product.objects.all()
	context = {
		"name":instance.name,
		"hi": instance

	}

	return render(req,'id.html',context)

def order_list(req):
	all_product = Product.objects.order_by("name")
	a1 = "Product by Name"

	return render(req,'order.html',{'ans':a1,'pro':all_product})

def post_update(req,id=None):
	if not req.user.is_staff or not req.user.is_superuser:
		raise Http404

	instance=get_object_or_404(Product,id=id)
	form = ProductForm(req.POST or None,instance = instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(req,"save")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(req,"not save")
		
	context = {
		"name":instance.name,
		"hi": instance,
		"form":form,

	}

	return render(req,'id.html',context)


def post_delete(req,id=None):
	if not req.user.is_staff or not req.user.is_superuser:
		raise Http404

	instance=get_object_or_404(Product,id=id)
	instance.delete()
	#message.success(req,"successfully delete")
	return redirect("posts:list")

def temp(req):
	json_response = json.dumps
	({'status':'ok','message':'hello world'})
	return HttpResponse(json_response)


# def my_view(req):
# 	username = req.POST['dhruvang9083']
# 	password = req.POST['hello']
# 	user = authenticate(req,username= username,password=password)
# 	if user is not None:
# 		login(req,user)
# 	else: 
# 		return ("Invalid")
