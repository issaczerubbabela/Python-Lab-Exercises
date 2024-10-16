from django.db import models

# Create your models here.

class Plant_Details(models.Model):
	plant_name = models.CharField(max_length=20)
	plant_type = models.CharField(max_length=20)
	plant_price = models.IntegerField()
	plant_benefits = models.CharField(max_length=50)
	