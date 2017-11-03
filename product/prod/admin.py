# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display  = ["name","price","quantity"]
	list_display_links = ["name","price"]
	search_fields = ["name"]
	list_editable =["quantity"]
	#list_editable1 =["price"]
	class Meta:
		model = Product
		'''
class ProductInline(admin.StackedInline):
	    model = Product
	    extra = 0
	    ordering = ('-name')
	'''

admin.site.register(Product,ProductModelAdmin)
#admin.site.register(ProductInline)
