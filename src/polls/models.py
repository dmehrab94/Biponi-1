from __future__ import unicode_literals

import datetime

from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.utils import timezone

class Product(models.Model):
	product_name=models.CharField(max_length=100)
	#give other product fields here

class Question(models.Model):
	#product=models.ForeignKey(Product,on_delete=models.CASCADE) eirokom kichu ekta lagbe import koraite hobe
	#question_title=models.CharField(max_length=50)
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now()-datetime.timedelta(days=1) #checking whether the date is today or yesterday

class Choice(models.Model):
	question=models.ForeignKey(Question,on_delete=models.CASCADE) #each Choice is related to a single Question
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text	
		
# Create your models here.
