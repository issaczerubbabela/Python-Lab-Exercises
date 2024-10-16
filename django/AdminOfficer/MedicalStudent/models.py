from django.db import models
from django import forms

# Create your models here.

program_choices = (
	('mbbs','MBBS'),
	('md', 'MD')
	)
payment_status = (
	('no','No'),
	('yes','Yes')
	)
class Student(models.Model):
	regno = models.IntegerField()
	name = models.CharField(max_length=30)
	program = models.CharField(max_length=5, choices=program_choices, default='MBBS')
	address = models.CharField(max_length=100)
	number = models.IntegerField()
	status = models.CharField(max_length=3, choices=payment_status, default='No')