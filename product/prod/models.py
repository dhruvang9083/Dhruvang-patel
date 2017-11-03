# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Product(models.Model):
	name = models.TextField(max_length = 50)
	price = models.IntegerField()
	image = models.FileField(null=True,blank=True)
	quantity = models.IntegerField(default=0)


	def __str__(self):
		return self.name
		return self.price
		return self.quantity
		return self.search

	def get_absolute_url(self):
		return reverse("prod:product",kwargs={'id':self.id})