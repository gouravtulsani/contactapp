# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.
class Contact(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	email = models.CharField(max_length=100,blank=True)
	company = models.CharField(max_length=100,blank=True)
	image = models.ImageField(blank=True)
	is_favorite = models.BooleanField(default=False)

	"""docstring for Contact"""
	def __str__(self):
		return self.name
		